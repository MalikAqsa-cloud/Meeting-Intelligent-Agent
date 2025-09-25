#!/bin/bash

echo "🆓 FREE Deployment Script for Meeting Intelligence Agent"
echo "======================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to deploy to Railway
deploy_railway() {
    echo -e "${BLUE}🚂 Deploying to Railway (Backend)...${NC}"
    echo ""
    echo "1. Go to https://railway.app"
    echo "2. Sign up with GitHub"
    echo "3. Click 'New Project'"
    echo "4. Select 'Deploy from GitHub repo'"
    echo "5. Choose your repository"
    echo "6. Railway will auto-deploy your backend"
    echo ""
    echo "Environment Variables to add in Railway:"
    echo "ASSEMBLYAI_API_KEY=your_key_here"
    echo "GEMINI_API_KEY=your_key_here"
    echo "TRELLO_API_KEY=your_key_here"
    echo "TRELLO_TOKEN=your_token_here"
    echo "TRELLO_LIST_ID=your_list_id_here"
    echo ""
    echo -e "${GREEN}✅ Railway will provide a URL like: https://your-app.railway.app${NC}"
}

# Function to deploy to Vercel
deploy_vercel() {
    echo -e "${BLUE}📱 Deploying to Vercel (Frontend)...${NC}"
    echo ""
    echo "Installing Vercel CLI..."
    npm install -g vercel 2>/dev/null || echo "Vercel CLI installation failed. Please install manually."
    echo ""
    echo "Deploying frontend..."
    cd frontend
    vercel --prod
    echo ""
    echo "Setting environment variable..."
    echo "Enter your Railway backend URL when prompted:"
    vercel env add VITE_API_URL production
    echo ""
    echo -e "${GREEN}✅ Frontend deployed to Vercel!${NC}"
    cd ..
}

# Function to deploy to Render
deploy_render() {
    echo -e "${BLUE}🌐 Deploying to Render (Backend)...${NC}"
    echo ""
    echo "1. Go to https://render.com"
    echo "2. Sign up with GitHub"
    echo "3. Click 'New +' → 'Web Service'"
    echo "4. Connect your GitHub repository"
    echo "5. Configure:"
    echo "   Build Command: pip install -r backend/requirements-prod.txt"
    echo "   Start Command: cd backend && uvicorn main:app --host 0.0.0.0 --port \$PORT"
    echo ""
    echo "Environment Variables to add in Render:"
    echo "ASSEMBLYAI_API_KEY=your_key_here"
    echo "GEMINI_API_KEY=your_key_here"
    echo "TRELLO_API_KEY=your_key_here"
    echo "TRELLO_TOKEN=your_token_here"
    echo "TRELLO_LIST_ID=your_list_id_here"
    echo ""
    echo -e "${GREEN}✅ Render will provide a URL like: https://your-app.onrender.com${NC}"
}

# Function to show free tier comparison
show_comparison() {
    echo -e "${YELLOW}📊 Free Tier Comparison${NC}"
    echo "========================"
    echo ""
    echo "🚂 Railway:"
    echo "   • $5 credit/month"
    echo "   • Auto-deployments"
    echo "   • Custom domains"
    echo "   • Both frontend & backend"
    echo ""
    echo "🌐 Render:"
    echo "   • 750 hours/month"
    echo "   • 512MB RAM"
    echo "   • Custom domains"
    echo "   • Backend only"
    echo "   • Services sleep after 15min inactivity"
    echo ""
    echo "📱 Vercel:"
    echo "   • 100GB bandwidth/month"
    echo "   • Unlimited deployments"
    echo "   • Global CDN"
    echo "   • Frontend only"
    echo ""
    echo -e "${GREEN}💡 Recommended: Railway + Vercel${NC}"
    echo "   • Railway for backend (free)"
    echo "   • Vercel for frontend (free)"
    echo "   • Total cost: $0/month"
}

# Main menu
echo ""
echo "Choose your FREE deployment option:"
echo "1) Railway (Backend) + Vercel (Frontend) - Recommended"
echo "2) Render (Backend) + Vercel (Frontend)"
echo "3) Railway Full Stack (Both)"
echo "4) Show free tier comparison"
echo "5) Complete deployment guide"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1)
        echo -e "${GREEN}🎯 Railway + Vercel Deployment${NC}"
        echo "=============================="
        deploy_railway
        echo ""
        deploy_vercel
        ;;
    2)
        echo -e "${GREEN}🎯 Render + Vercel Deployment${NC}"
        echo "=============================="
        deploy_render
        echo ""
        deploy_vercel
        ;;
    3)
        echo -e "${GREEN}🎯 Railway Full Stack Deployment${NC}"
        echo "=================================="
        deploy_railway
        echo ""
        echo "For frontend on Railway:"
        echo "1. Create another Railway project"
        echo "2. Select your frontend folder"
        echo "3. Railway will auto-detect Node.js"
        ;;
    4)
        show_comparison
        ;;
    5)
        echo -e "${BLUE}📚 Complete Deployment Guide${NC}"
        echo "=============================="
        echo ""
        echo "1. Push your code to GitHub:"
        echo "   git add ."
        echo "   git commit -m 'Ready for deployment'"
        echo "   git push origin main"
        echo ""
        echo "2. Deploy backend to Railway:"
        echo "   • Go to railway.app"
        echo "   • Connect GitHub repo"
        echo "   • Add environment variables"
        echo ""
        echo "3. Deploy frontend to Vercel:"
        echo "   • Install Vercel CLI: npm install -g vercel"
        echo "   • Run: vercel --prod"
        echo "   • Set VITE_API_URL environment variable"
        echo ""
        echo "4. Test your deployment:"
        echo "   • Check backend health: https://your-app.railway.app/"
        echo "   • Check frontend: https://your-app.vercel.app"
        echo "   • Test file upload functionality"
        ;;
    *)
        echo -e "${RED}Invalid choice. Please run the script again.${NC}"
        ;;
esac

echo ""
echo -e "${GREEN}🎉 Happy Deploying! Your app will be live for FREE!${NC}"
