# 🚀 Meeting Intelligence Agent - Deployment Guide

This guide covers multiple deployment options for the Meeting Intelligence Agent project.

## 📋 Prerequisites

- **API Keys**: Get your API keys from:
  - [AssemblyAI](https://www.assemblyai.com/) (Free tier available)
  - [Google Gemini](https://makersuite.google.com/app/apikey)
  - [Trello](https://trello.com/app-key)
- **GitHub Repository**: Push your code to GitHub
- **Domain** (optional): For custom domain setup

## 🎯 Deployment Options

### 1. 🌐 Vercel (Frontend) + Render (Backend) - Recommended

#### Frontend on Vercel
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy frontend
cd frontend
vercel --prod

# Set environment variable
vercel env add VITE_API_URL production
# Enter your backend URL when prompted
```

#### Backend on Render
1. Go to [Render](https://render.com)
2. Connect your GitHub repository
3. Create a new **Web Service**
4. Configure:
   - **Build Command**: `pip install -r backend/requirements-prod.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     ```
     ASSEMBLYAI_API_KEY=your_key
     GEMINI_API_KEY=your_key
     TRELLO_API_KEY=your_key
     TRELLO_TOKEN=your_token
     TRELLO_LIST_ID=your_list_id
     ```

### 2. 🚂 Railway (Full Stack)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway up

# Set environment variables
railway variables set ASSEMBLYAI_API_KEY=your_key
railway variables set GEMINI_API_KEY=your_key
railway variables set TRELLO_API_KEY=your_key
railway variables set TRELLO_TOKEN=your_token
railway variables set TRELLO_LIST_ID=your_list_id
```

### 3. 🐳 Docker Deployment

#### Local Docker
```bash
# Build and run
docker-compose up --build

# Access:
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
```

#### Docker on Cloud
- **DigitalOcean App Platform**
- **AWS ECS**
- **Google Cloud Run**
- **Azure Container Instances**

### 4. ☁️ AWS/GCP/Azure

#### AWS (Elastic Beanstalk + S3)
```bash
# Backend on Elastic Beanstalk
eb init
eb create production

# Frontend on S3 + CloudFront
aws s3 sync frontend/dist s3://your-bucket
```

#### Google Cloud Platform
```bash
# Backend on Cloud Run
gcloud run deploy --source backend

# Frontend on Firebase Hosting
firebase deploy
```

## 🔧 Environment Variables

### Backend (.env)
```env
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
GEMINI_API_KEY=your_gemini_api_key
TRELLO_API_KEY=your_trello_api_key
TRELLO_TOKEN=your_trello_token
TRELLO_LIST_ID=your_trello_list_id
```

### Frontend (.env)
```env
VITE_API_URL=https://your-backend-url.com
```

## 📱 Quick Deploy Script

Use the included deployment script:

```bash
./deploy.sh
```

Choose from:
1. Vercel (Frontend)
2. Render (Backend)
3. Railway (Full stack)
4. Docker (Local)
5. Complete guide

## 🔍 Testing Your Deployment

1. **Health Check**: Visit `https://your-backend-url.com/`
2. **API Docs**: Visit `https://your-backend-url.com/docs`
3. **Frontend**: Visit your frontend URL
4. **Upload Test**: Try uploading a small audio file

## 🛠 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure backend CORS is configured for your frontend domain
   - Check that `VITE_API_URL` points to the correct backend

2. **Environment Variables**
   - Verify all API keys are set correctly
   - Check that environment variables are properly configured

3. **Build Failures**
   - Check Python/Node.js versions
   - Verify all dependencies are in requirements.txt

4. **File Upload Issues**
   - Check file size limits
   - Verify supported file formats

### Debug Commands

```bash
# Check backend logs
railway logs  # Railway
render logs  # Render

# Test API endpoints
curl https://your-backend-url.com/
curl -X POST https://your-backend-url.com/process-audio
```

## 📊 Monitoring & Maintenance

### Health Checks
- Backend: `GET /` returns status
- Frontend: Static file serving

### Logs
- Monitor API usage
- Track error rates
- Monitor file uploads

### Scaling
- **Render**: Auto-scales based on traffic
- **Railway**: Manual scaling available
- **Vercel**: Automatic edge scaling

## 🔒 Security Considerations

1. **API Keys**: Never commit to repository
2. **HTTPS**: Always use HTTPS in production
3. **CORS**: Configure CORS properly
4. **File Uploads**: Implement size limits
5. **Rate Limiting**: Consider implementing rate limits

## 💰 Cost Estimation

### Free Tiers
- **Vercel**: 100GB bandwidth/month
- **Render**: 750 hours/month
- **Railway**: $5 credit/month

### Paid Plans
- **Vercel Pro**: $20/month
- **Render**: $7/month per service
- **Railway**: Pay-as-you-go

## 🎯 Production Checklist

- [ ] All API keys configured
- [ ] HTTPS enabled
- [ ] CORS properly configured
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Health checks working
- [ ] File upload limits set
- [ ] Monitoring setup
- [ ] Backup strategy
- [ ] Domain configured (optional)

## 📞 Support

If you encounter issues:
1. Check the logs
2. Verify environment variables
3. Test API endpoints directly
4. Check platform-specific documentation

---

**Happy Deploying! 🚀**
