import os
import google.generativeai as genai
import logging
from typing import Dict, List, Optional
import json

logger = logging.getLogger(__name__)

class SummarizationAgent:
    """
    Agent responsible for generating meeting summaries and extracting action items using Google Gemini
    """
    
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            logger.warning("GEMINI_API_KEY not found. Using demo mode.")
            self.demo_mode = True
        else:
            self.demo_mode = False
            # Configure Gemini
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    async def process_transcript(self, transcript: str) -> Optional[Dict[str, any]]:
        """
        Process transcript to generate summary and extract action items
        
        Args:
            transcript: Raw transcript text
            
        Returns:
            Dict containing summary and action_items or None if failed
        """
        try:
            logger.info("Starting transcript processing")
            
            if self.demo_mode:
                # Return demo summary and action items
                demo_result = {
                    "summary": "This was a productive weekly team meeting focused on product launch preparation and budget planning. The team discussed upcoming deadlines, resource allocation, and coordination between departments. Key decisions were made regarding marketing materials, product demos, and budget review processes.",
                    "action_items": [
                        "Sarah will finalize the marketing materials by Friday",
                        "John will prepare a product demo for the sales team", 
                        "Finance team will review Q2 budget allocation",
                        "Marketing team will submit campaign proposal by next week"
                    ]
                }
                logger.info("Demo mode: Returning sample summary and action items")
                return demo_result
            
            # Create prompt for Gemini
            prompt = f"""
            Please analyze the following meeting transcript and provide:
            
            1. A concise summary of the meeting (2-3 paragraphs)
            2. A clear list of action items with responsible parties and deadlines where mentioned
            
            Meeting Transcript:
            {transcript}
            
            Please format your response as JSON with the following structure:
            {{
                "summary": "Meeting summary here...",
                "action_items": [
                    "Action item 1",
                    "Action item 2",
                    "Action item 3"
                ]
            }}
            
            For action items, extract only concrete, actionable tasks that were discussed. 
            If no specific action items were mentioned, return an empty array.
            """
            
            # Generate response using Gemini
            logger.info("Sending request to Gemini API...")
            response = self.model.generate_content(prompt)
            
            if not response.text:
                logger.error("Empty response from Gemini")
                return None
            
            # Parse JSON response
            try:
                # Clean the response text (remove markdown formatting if present)
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                
                result = json.loads(response_text)
                
                # Validate response structure
                if "summary" not in result or "action_items" not in result:
                    logger.error("Invalid response structure from Gemini")
                    return None
                
                logger.info(f"Successfully processed transcript. Found {len(result['action_items'])} action items")
                return result
                
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse Gemini response as JSON: {str(e)}")
                logger.error(f"Raw response: {response.text}")
                
                # Fallback: try to extract information manually
                return self._fallback_extraction(response.text)
                
        except Exception as e:
            logger.error(f"Error processing transcript: {str(e)}")
            return None
    
    def _fallback_extraction(self, response_text: str) -> Dict[str, any]:
        """
        Fallback method to extract summary and action items from unstructured text
        """
        try:
            lines = response_text.split('\n')
            summary_lines = []
            action_items = []
            in_summary = False
            in_action_items = False
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Detect summary section
                if 'summary' in line.lower() or 'meeting summary' in line.lower():
                    in_summary = True
                    in_action_items = False
                    continue
                
                # Detect action items section
                if 'action' in line.lower() and 'item' in line.lower():
                    in_summary = False
                    in_action_items = True
                    continue
                
                # Collect content
                if in_summary and not in_action_items:
                    summary_lines.append(line)
                elif in_action_items:
                    # Look for bullet points or numbered items
                    if line.startswith(('-', '*', '•', '1.', '2.', '3.')):
                        action_items.append(line.lstrip('-*•123456789. '))
            
            return {
                "summary": ' '.join(summary_lines) if summary_lines else "Summary extraction failed",
                "action_items": action_items if action_items else []
            }
            
        except Exception as e:
            logger.error(f"Fallback extraction failed: {str(e)}")
            return {
                "summary": "Failed to generate summary",
                "action_items": []
            }
