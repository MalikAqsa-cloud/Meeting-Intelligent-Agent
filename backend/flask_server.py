from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    """Health check endpoint"""
    return jsonify({
        "message": "Meeting Intelligence Agent API is running!",
        "status": "success"
    })

@app.route('/process-audio', methods=['POST'])
def process_audio():
    """Demo endpoint for audio processing"""
    return jsonify({
        "transcript": "This is a demo transcript. In the full application, this would show the actual transcribed text from your uploaded audio file.",
        "summary": "This is a demo summary. In the full application, this would show an AI-generated summary of your meeting content.",
        "action_items": [
            "Follow up with the client about project requirements",
            "Schedule team meeting for next week",
            "Review budget allocation for Q4"
        ],
        "status": "success"
    })

@app.route('/send-to-trello', methods=['POST'])
def send_to_trello():
    """Demo endpoint for Trello integration"""
    return jsonify({
        "message": "Successfully created 3 tasks in Trello (Demo Mode)",
        "created_cards": [
            {"id": "demo1", "name": "Follow up with the client", "url": "https://trello.com/demo1"},
            {"id": "demo2", "name": "Schedule team meeting", "url": "https://trello.com/demo2"},
            {"id": "demo3", "name": "Review budget allocation", "url": "https://trello.com/demo3"}
        ],
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
