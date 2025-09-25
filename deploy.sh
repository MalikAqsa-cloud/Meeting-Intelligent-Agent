#!/bin/bash

echo "🚀 Meeting Intelligence Agent Deployment Script"
echo "=============================================="

# Function to deploy to different platforms
deploy_vercel() {
    echo "📱 Deploying Frontend to Vercel..."
    cd frontend
    npx vercel --prod
    cd ..
}

deploy_render() {
    echo "🔧 Deploying Backend to Render..."
    echo "1. Go to https://render.com"
    echo "2. Connect your GitHub repository"
    echo "3. Create a new Web Service"
    echo "4. Use these settings:"
    echo "   - Build Command: pip install -r backend/requirements-prod.txt"
    echo "   - Start Command: cd backend && uvicorn main:app --host 0.0.0.0 --port \$PORT"
    echo "   - Add environment variables from backend/.env"
}

deploy_railway() {
    echo "🚂 Deploying to Railway..."
    echo "1. Install Railway CLI: npm install -g @railway/cli"
    echo "2. Login: railway login"
    echo "3. Deploy: railway up"
}

deploy_docker() {
    echo "🐳 Building Docker containers..."
    docker-compose build
    echo "🚀 Starting services..."
    docker-compose up -d
    echo "✅ Services running on:"
    echo "   Frontend: http://localhost:3000"
    echo "   Backend: http://localhost:8000"
}

# Main menu
echo ""
echo "Choose deployment option:"
echo "1) Vercel (Frontend only)"
echo "2) Render (Backend)"
echo "3) Railway (Full stack)"
echo "4) Docker (Local)"
echo "5) All platforms guide"
echo ""

read -p "Enter your choice (1-5): " choice

case $choice in
    1) deploy_vercel ;;
    2) deploy_render ;;
    3) deploy_railway ;;
    4) deploy_docker ;;
    5) 
        echo "📚 Complete Deployment Guide:"
        echo "============================="
        deploy_vercel
        echo ""
        deploy_render
        echo ""
        deploy_railway
        ;;
    *) echo "Invalid choice. Please run the script again." ;;
esac
