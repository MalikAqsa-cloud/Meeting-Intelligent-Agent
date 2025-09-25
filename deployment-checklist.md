# ✅ Railway + Vercel Deployment Checklist

## 📋 Complete Deployment Steps:

### Phase 1: GitHub Setup
- [ ] 1. Go to https://github.com/new
- [ ] 2. Create repository: `meeting-intelligence-agent`
- [ ] 3. Make it PUBLIC
- [ ] 4. Don't initialize with README
- [ ] 5. Copy repository URL
- [ ] 6. Run these commands:
  ```bash
  git remote add origin https://github.com/YOUR_USERNAME/meeting-intelligence-agent.git
  git branch -M main
  git push -u origin main
  ```

### Phase 2: Railway Backend Deployment
- [ ] 1. Go to https://railway.app
- [ ] 2. Sign up with GitHub
- [ ] 3. Click "New Project"
- [ ] 4. Select "Deploy from GitHub repo"
- [ ] 5. Choose your repository
- [ ] 6. Wait for auto-deployment
- [ ] 7. Copy your Railway URL: `https://your-app.railway.app`
- [ ] 8. Test: Visit `https://your-app.railway.app/docs`

### Phase 3: Vercel Frontend Deployment
- [ ] 1. Go to https://vercel.com
- [ ] 2. Sign up with GitHub
- [ ] 3. Click "New Project"
- [ ] 4. Import your repository
- [ ] 5. Configure:
  - Root Directory: `frontend`
  - Build Command: `npm run build`
  - Output Directory: `dist`
- [ ] 6. Add environment variable:
  ```
  VITE_API_URL=https://your-railway-app.railway.app
  ```
- [ ] 7. Deploy
- [ ] 8. Copy your Vercel URL: `https://your-app.vercel.app`

### Phase 4: Testing
- [ ] 1. Test backend: `https://your-app.railway.app/`
- [ ] 2. Test API docs: `https://your-app.railway.app/docs`
- [ ] 3. Test frontend: `https://your-app.vercel.app`
- [ ] 4. Upload audio file and test full functionality

## 🎯 Your Final URLs:
- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-app.railway.app`
- **API Docs**: `https://your-app.railway.app/docs`

## 🆓 Cost: $0/month (Free tiers)
