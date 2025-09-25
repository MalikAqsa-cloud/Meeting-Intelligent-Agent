import os
import assemblyai as aai
import tempfile
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class TranscriptionAgent:
    """
    Agent responsible for converting audio files to text using AssemblyAI
    """
    
    def __init__(self):
        self.api_key = os.getenv("ASSEMBLYAI_API_KEY")
        if not self.api_key:
            logger.warning("ASSEMBLYAI_API_KEY not found. Using demo mode.")
            self.demo_mode = True
        else:
            self.demo_mode = False
            # Configure AssemblyAI
            aai.settings.api_key = self.api_key
    
    async def transcribe_audio(self, audio_file) -> Optional[str]:
        """
        Transcribe uploaded audio file to text
        
        Args:
            audio_file: FastAPI UploadFile object
            
        Returns:
            str: Transcribed text or None if failed
        """
        try:
            logger.info(f"Starting transcription for file: {audio_file.filename}")
            
            if self.demo_mode:
                # Return demo transcript
                demo_transcript = """
                Welcome to our weekly team meeting. Today we discussed several important topics including the upcoming product launch, budget planning for Q2, and the new marketing campaign. 

                Sarah mentioned that the product launch is scheduled for next month and we need to finalize the marketing materials. John suggested we should also prepare a demo for the sales team.

                We also talked about the budget allocation. The marketing department needs additional funds for the campaign, and we need to review the current spending patterns.

                Action items from this meeting include:
                1. Sarah will finalize the marketing materials by Friday
                2. John will prepare a product demo for the sales team
                3. Finance team will review Q2 budget allocation
                4. Marketing team will submit campaign proposal by next week
                """
                logger.info("Demo mode: Returning sample transcript")
                return demo_transcript.strip()
            
            # Save uploaded file to temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{audio_file.filename}") as temp_file:
                content = await audio_file.read()
                temp_file.write(content)
                temp_file_path = temp_file.name
            
            try:
                # Create AssemblyAI transcriber
                transcriber = aai.Transcriber()
                
                # Transcribe the audio file
                logger.info("Uploading file to AssemblyAI...")
                transcript = transcriber.transcribe(temp_file_path)
                
                # Wait for transcription to complete
                logger.info("Waiting for transcription to complete...")
                while transcript.status not in [aai.TranscriptStatus.completed, aai.TranscriptStatus.error]:
                    transcript = transcriber.get_transcript(transcript.id)
                
                if transcript.status == aai.TranscriptStatus.error:
                    logger.error(f"Transcription failed: {transcript.error}")
                    return None
                
                logger.info("Transcription completed successfully")
                return transcript.text
                
            finally:
                # Clean up temporary file
                os.unlink(temp_file_path)
                
        except Exception as e:
            logger.error(f"Error during transcription: {str(e)}")
            return None
