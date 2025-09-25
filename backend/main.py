from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from dotenv import load_dotenv
from typing import List, Dict, Any
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Meeting Intelligence Agent",
    description="AI-powered meeting analysis with transcription, summarization, and task creation",
    version="1.0.0"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents with error handling
transcription_agent = None
summarization_agent = None
trello_agent = None

try:
    from agents.transcription_agent import TranscriptionAgent
    transcription_agent = TranscriptionAgent()
    logger.info("Transcription agent initialized successfully")
except Exception as e:
    logger.warning(f"Failed to initialize transcription agent: {e}")

try:
    from agents.summarization_agent import SummarizationAgent
    summarization_agent = SummarizationAgent()
    logger.info("Summarization agent initialized successfully")
except Exception as e:
    logger.warning(f"Failed to initialize summarization agent: {e}")

try:
    from agents.trello_agent import TrelloAgent
    trello_agent = TrelloAgent()
    logger.info("Trello agent initialized successfully")
except Exception as e:
    logger.warning(f"Failed to initialize Trello agent: {e}")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Meeting Intelligence Agent API is running!",
        "agents": {
            "transcription": transcription_agent is not None,
            "summarization": summarization_agent is not None,
            "trello": trello_agent is not None
        }
    }

@app.post("/process-audio")
async def process_audio(file: UploadFile = File(...)):
    """
    Process uploaded audio file through the complete pipeline:
    1. Transcribe audio to text
    2. Generate summary and extract action items
    3. Return structured data for frontend
    """
    try:
        # Validate file type
        if not file.filename.lower().endswith(('.mp3', '.wav', '.m4a', '.flac')):
            raise HTTPException(status_code=400, detail="Only audio files (.mp3, .wav, .m4a, .flac) are supported")
        
        logger.info(f"Processing audio file: {file.filename}")
        
        # Check if agents are available
        if not transcription_agent:
            raise HTTPException(status_code=500, detail="Transcription agent not available. Please check API keys.")
        
        if not summarization_agent:
            raise HTTPException(status_code=500, detail="Summarization agent not available. Please check API keys.")
        
        # Step 1: Transcribe audio
        logger.info("Starting transcription...")
        transcript = await transcription_agent.transcribe_audio(file)
        
        if not transcript:
            raise HTTPException(status_code=500, detail="Transcription failed")
        
        # Step 2: Generate summary and extract action items
        logger.info("Generating summary and extracting action items...")
        summary_data = await summarization_agent.process_transcript(transcript)
        
        if not summary_data:
            raise HTTPException(status_code=500, detail="Summarization failed")
        
        # Return structured response
        response = {
            "transcript": transcript,
            "summary": summary_data.get("summary", ""),
            "action_items": summary_data.get("action_items", []),
            "status": "success"
        }
        
        logger.info("Audio processing completed successfully")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error processing audio: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.post("/send-to-trello")
async def send_to_trello(action_items: List[str]):
    """
    Send action items to Trello as task cards
    """
    try:
        if not action_items:
            raise HTTPException(status_code=400, detail="No action items provided")
        
        if not trello_agent:
            raise HTTPException(status_code=500, detail="Trello agent not available. Please check API keys.")
        
        logger.info(f"Sending {len(action_items)} action items to Trello")
        
        results = await trello_agent.create_tasks(action_items)
        
        return {
            "message": f"Successfully created {len(results)} tasks in Trello",
            "created_cards": results,
            "status": "success"
        }
        
    except Exception as e:
        logger.error(f"Error creating Trello tasks: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create Trello tasks: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
