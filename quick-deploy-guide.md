# 🚀 Quick Deployment Guide - Get Public URLs

## Option 1: Render (Easiest - No GitHub Required)

### Backend Deployment:
1. Go to https://render.com
2. Sign up with email
3. Click "New +" → "Web Service"
4. Choose "Build and deploy from a Git repository"
5. Connect your GitHub (or upload code directly)
6. Configure:
   - **Build Command**: `pip install -r backend/requirements-prod.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Add environment variables (optional for demo mode)
8. Deploy!

### Frontend Deployment:
1. In Render, click "New +" → "Static Site"
2. Connect your repository
3. Configure:
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/dist`
4. Deploy!

## Option 2: Railway (Requires GitHub)

### Steps:
1. Create GitHub repository
2. Push your code
3. Deploy to Railway
4. Deploy to Vercel

## Option 3: Netlify (Frontend Only - Quick Test)

### Steps:
1. Go to https://netlify.com
2. Drag and drop your `frontend/dist` folder
3. Get instant URL!

## 🎯 Your URLs Will Look Like:

- **Backend**: `https://your-app-name.onrender.com`
- **Frontend**: `https://your-app-name.onrender.com` (static)
- **API Docs**: `https://your-app-name.onrender.com/docs`

## ⚡ Quick Test URLs (Demo Mode):

Since your app works in demo mode, you can deploy without API keys and test immediately!
