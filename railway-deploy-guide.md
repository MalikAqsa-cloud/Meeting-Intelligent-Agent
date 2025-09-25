# 🚂 Railway Backend Deployment Guide

## Step-by-Step Instructions:

### 1. Go to Railway
- Visit: https://railway.app
- Sign up with GitHub (use the same account as your repository)

### 2. Create New Project
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose your "meeting-intelligence-agent" repository

### 3. Railway Auto-Detection
- Railway will automatically detect it's a Python project
- It will use the `backend/requirements-prod.txt` file
- It will run: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### 4. Environment Variables (Optional for Demo)
- Go to your project settings
- Add these variables (only if you have API keys):
  ```
  ASSEMBLYAI_API_KEY=your_key_here
  GEMINI_API_KEY=your_key_here
  TRELLO_API_KEY=your_key_here
  TRELLO_TOKEN=your_token_here
  TRELLO_LIST_ID=your_list_id_here
  ```

### 5. Deploy!
- Railway will automatically deploy your backend
- You'll get a URL like: `https://your-app-name.railway.app`

### 6. Test Your Backend
- Visit: `https://your-app-name.railway.app/`
- API Docs: `https://your-app-name.railway.app/docs`

## 🎉 Your Backend URL will be:
`https://your-app-name.railway.app`
