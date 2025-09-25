# Meeting Intelligence Agent

A complete AI-powered meeting analysis application that transcribes audio, generates summaries, and creates actionable task cards in Trello. Built with React frontend and FastAPI backend using multi-agent architecture.

## 🎯 Features

- **Audio Transcription**: Convert meeting audio to text using AssemblyAI
- **AI Summarization**: Generate meeting summaries using Google Gemini 1.5 Flash
- **Action Item Extraction**: Automatically identify and extract actionable tasks
- **Trello Integration**: Create task cards directly in Trello boards
- **Modern UI**: Clean, responsive interface built with React and TailwindCSS
- **Real-time Processing**: Live status updates and error handling

## 🛠 Tech Stack

### Frontend
- **React 18** with Vite for fast development
- **TailwindCSS** for modern, responsive styling
- **Component-based architecture** for maintainability

### Backend
- **FastAPI** (Python 3.12) for high-performance API
- **Multi-agent architecture** with specialized agents:
  - Transcription Agent (AssemblyAI)
  - Summarization Agent (Google Gemini)
  - Trello Agent (Trello REST API)
- **CORS-enabled** for seamless frontend integration

### APIs & Services
- **AssemblyAI**: Speech-to-text transcription
- **Google Gemini 1.5 Flash**: AI-powered text analysis
- **Trello REST API**: Task management integration

## 📁 Project Structure

```
Multi_Agent/
├── backend/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── transcription_agent.py
│   │   ├── summarization_agent.py
│   │   └── trello_agent.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.jsx
│   │   │   ├── LoadingSpinner.jsx
│   │   │   ├── ErrorMessage.jsx
│   │   │   ├── TranscriptDisplay.jsx
│   │   │   ├── SummaryDisplay.jsx
│   │   │   └── ActionItemsDisplay.jsx
│   │   ├── App.jsx
│   │   └── index.css
│   ├── package.json
│   ├── tailwind.config.js
│   └── postcss.config.js
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.12+**
- **Node.js 18+**
- **npm** or **yarn**

### 1. Clone and Setup

```bash
git clone <your-repo-url>
cd Multi_Agent
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your API keys (see API Setup section below)
```

### 3. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 4. Run Backend

```bash
cd backend
source venv/bin/activate  # If not already activated
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application will be available at:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## �� API Setup

### 1. AssemblyAI (Free Tier Available)
1. Visit [AssemblyAI](https://www.assemblyai.com/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Add to `.env`: `ASSEMBLYAI_API_KEY=your_key_here`

### 2. Google Gemini
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add to `.env`: `GEMINI_API_KEY=your_key_here`

### 3. Trello Integration
1. Visit [Trello App Key](https://trello.com/app-key)
2. Get your API Key and Token
3. Create a board and list for tasks
4. Get the List ID from the URL: `https://trello.com/b/BOARD_ID/LIST_NAME`
5. Add to `.env`:
   ```
   TRELLO_API_KEY=your_api_key
   TRELLO_TOKEN=your_token
   TRELLO_LIST_ID=your_list_id
   ```

### Complete .env Example

```env
# AssemblyAI API Key
ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here

# Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Trello API Credentials
TRELLO_API_KEY=your_trello_api_key_here
TRELLO_TOKEN=your_trello_token_here
TRELLO_LIST_ID=your_trello_list_id_here
```

## 📱 Usage

1. **Upload Audio**: Drag and drop or click to upload meeting audio (.mp3, .wav, .m4a, .flac)
2. **Processing**: Wait for AI agents to transcribe and analyze the content
3. **Review Results**: View transcript, summary, and extracted action items
4. **Create Tasks**: Click "Send to Trello" to create task cards for action items

## 🚀 Deployment

### Frontend (Vercel)

1. **Connect Repository**:
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Deploy from frontend directory
   cd frontend
   vercel
   ```

2. **Environment Variables**: Set `VITE_API_URL` to your backend URL

3. **Build Settings**:
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

### Backend (Render)

1. **Create New Web Service**:
   - Connect your GitHub repository
   - Choose "Web Service"

2. **Build Settings**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

3. **Environment Variables**: Add all API keys from your `.env` file

### Alternative: Railway

1. **Connect Repository** to Railway
2. **Add Environment Variables** for all API keys
3. **Deploy**: Railway will automatically detect Python and deploy

## �� Development

### Backend Development

```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

### Frontend Development

```bash
cd frontend
npm run dev
```

### API Testing

Visit http://localhost:8000/docs for interactive API documentation.

## 🧪 Testing the Application

1. **Test Audio Upload**: Use a sample meeting recording
2. **Verify Transcription**: Check accuracy of speech-to-text
3. **Review Summary**: Ensure AI-generated summary is coherent
4. **Test Action Items**: Verify extraction of actionable tasks
5. **Trello Integration**: Confirm task cards are created successfully

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure backend is running on port 8000
2. **API Key Errors**: Verify all environment variables are set correctly
3. **File Upload Issues**: Check file format and size limits
4. **Trello Connection**: Verify API credentials and list ID

### Debug Mode

Enable debug logging in backend:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Future Enhancements

- [ ] Support for video files
- [ ] Multiple language support
- [ ] Custom AI model fine-tuning
- [ ] Integration with other task management tools
- [ ] Real-time collaboration features
- [ ] Advanced analytics and insights

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 🙏 Acknowledgments

- AssemblyAI for speech-to-text capabilities
- Google Gemini for AI-powered text analysis
- Trello for task management integration
- React and FastAPI communities for excellent documentation

---
# Meeting-Intelligent-Agent
