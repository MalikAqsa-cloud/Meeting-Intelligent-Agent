# 🚀 DEPLOY NOW - Get Your URLs!

## ✅ Step-by-Step Deployment

### 1. Railway Backend (5 minutes)
- Go to: https://railway.app
- Sign up with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select: `Meeting-Intelligent-Agent`
- Wait for deployment
- Copy your URL: `https://meeting-intelligent-agent-production-xxxx.up.railway.app`

### 2. Vercel Frontend (5 minutes)
- Go to: https://vercel.com
- Sign up with GitHub
- Click "New Project" → Import `Meeting-Intelligent-Agent`
- Configure:
  - Root Directory: `frontend`
  - Build Command: `npm run build`
  - Output Directory: `dist`
- Add Environment Variable:
  ```
  VITE_API_URL=https://your-railway-url.up.railway.app
  ```
- Deploy!

### 3. Test Your App
- Visit your Vercel URL
- Upload an audio file
- Test the full functionality!

## 🎉 Your URLs Will Be:
- **Main App**: `https://meeting-intelligent-agent.vercel.app`
- **Backend API**: `https://meeting-intelligent-agent-production-xxxx.up.railway.app`
- **API Docs**: `https://your-backend-url.up.railway.app/docs`

## 💡 Pro Tips:
- Your app works in demo mode (no API keys needed for testing)
- Both platforms have free tiers
- Deployment takes 5-10 minutes total
- You can add real API keys later through platform settings

## 🆘 Need Help?
- Railway docs: https://docs.railway.app
- Vercel docs: https://vercel.com/docs
