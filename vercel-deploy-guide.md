# 📱 Vercel Frontend Deployment Guide

## Step-by-Step Instructions:

### 1. Go to Vercel
- Visit: https://vercel.com
- Sign up with GitHub (use the same account as your repository)

### 2. Import Project
- Click "New Project"
- Import your "meeting-intelligence-agent" repository
- Vercel will auto-detect it's a Vite React project

### 3. Configure Build Settings
- **Framework Preset**: Vite
- **Root Directory**: `frontend`
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`

### 4. Environment Variables
- Add this environment variable:
  ```
  VITE_API_URL=https://your-railway-app.railway.app
  ```
- Replace `your-railway-app` with your actual Railway app name

### 5. Deploy!
- Click "Deploy"
- Vercel will build and deploy your frontend
- You'll get a URL like: `https://your-app-name.vercel.app`

### 6. Test Your Frontend
- Visit: `https://your-app-name.vercel.app`
- Upload an audio file to test the full functionality

## 🎉 Your Frontend URL will be:
`https://your-app-name.vercel.app`

## 🔗 Complete URLs:
- **Frontend**: `https://your-app-name.vercel.app`
- **Backend**: `https://your-railway-app.railway.app`
- **API Docs**: `https://your-railway-app.railway.app/docs`
