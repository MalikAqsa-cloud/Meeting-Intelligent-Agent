# 🆓 FREE Deployment Guide - Meeting Intelligence Agent

## 🎯 Best Free Platform Combinations

### Option 1: Railway + Vercel (Recommended)
- **Backend**: Railway (Free $5/month credit)
- **Frontend**: Vercel (Free tier)
- **Total Cost**: $0/month

### Option 2: Render + Vercel
- **Backend**: Render (Free 750 hours/month)
- **Frontend**: Vercel (Free tier)
- **Total Cost**: $0/month

### Option 3: Railway Full Stack
- **Both**: Railway (Free $5/month credit)
- **Total Cost**: $0/month

## 🚂 Railway Deployment (Backend)

### Step 1: Prepare Your Repository
```bash
# Make sure your code is on GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy to Railway
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will auto-detect Python and deploy

### Step 3: Configure Environment Variables
In Railway dashboard:
```
ASSEMBLYAI_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
TRELLO_API_KEY=your_key_here
TRELLO_TOKEN=your_token_here
TRELLO_LIST_ID=your_list_id_here
```

### Step 4: Get Your Backend URL
Railway will provide a URL like: `https://your-app-name.railway.app`

## 📱 Vercel Deployment (Frontend)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Deploy Frontend
```bash
cd frontend
vercel --prod
```

### Step 3: Set Environment Variable
```bash
vercel env add VITE_API_URL production
# Enter your Railway backend URL when prompted
```

## 🌐 Render Deployment (Alternative Backend)

### Step 1: Deploy to Render
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Build Command**: `pip install -r backend/requirements-prod.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 2: Environment Variables
Add in Render dashboard:
```
ASSEMBLYAI_API_KEY=your_key
GEMINI_API_KEY=your_key
TRELLO_API_KEY=your_key
TRELLO_TOKEN=your_token
TRELLO_LIST_ID=your_list_id
```

## 🆓 Completely Free Alternatives

### 1. **Heroku** (Limited Free Tier)
- **Free Tier**: 550-1000 dyno hours/month
- **Note**: Heroku removed free tier in 2022

### 2. **Netlify** (Frontend Only)
- **Free Tier**: 100GB bandwidth/month
- **Best for**: Static sites only

### 3. **Firebase Hosting** (Frontend Only)
- **Free Tier**: 10GB storage, 10GB/month transfer
- **Best for**: Static sites only

### 4. **GitHub Pages** (Frontend Only)
- **Free Tier**: Unlimited
- **Best for**: Static sites only

## 🎯 Quick Start Commands

### Railway + Vercel Setup
```bash
# 1. Deploy backend to Railway
# Go to railway.app and connect GitHub repo

# 2. Deploy frontend to Vercel
cd frontend
npm install -g vercel
vercel --prod

# 3. Set environment variable
vercel env add VITE_API_URL production
# Enter your Railway URL: https://your-app.railway.app
```

## 🔧 Free Tier Limitations

### Railway
- ✅ $5 credit/month (usually sufficient)
- ✅ Automatic deployments
- ✅ Custom domains
- ❌ Limited to $5 worth of usage

### Render
- ✅ 750 hours/month free
- ✅ 512MB RAM
- ✅ Custom domains
- ❌ Services sleep after 15 min inactivity

### Vercel
- ✅ 100GB bandwidth/month
- ✅ Unlimited deployments
- ✅ Global CDN
- ❌ No server-side functions (frontend only)

## 💡 Pro Tips for Free Deployment

1. **Optimize Your App**:
   - Use demo mode when API keys aren't available
   - Implement efficient caching
   - Minimize file sizes

2. **Monitor Usage**:
   - Check Railway usage dashboard
   - Monitor Render hours
   - Track Vercel bandwidth

3. **Backup Strategy**:
   - Keep code on GitHub
   - Export environment variables
   - Document deployment steps

## 🚨 Important Notes

- **Railway**: Services may stop if you exceed $5 credit
- **Render**: Services sleep after inactivity (cold start delay)
- **Vercel**: Perfect for frontend, no backend hosting
- **Always**: Keep your GitHub repository updated

## 🎉 Success Checklist

- [ ] Backend deployed and accessible
- [ ] Frontend deployed and accessible
- [ ] Environment variables configured
- [ ] API endpoints working
- [ ] File upload functionality tested
- [ ] Custom domain configured (optional)

---

**Total Monthly Cost: $0** 🎉
