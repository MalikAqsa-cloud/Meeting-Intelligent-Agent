#!/bin/bash

echo "🌐 Getting Public URLs for Meeting Intelligence Agent"
echo "=================================================="
echo ""

echo "📋 Choose your deployment method:"
echo "1) Render (Easiest - No GitHub required)"
echo "2) Railway + Vercel (Requires GitHub)"
echo "3) Netlify (Frontend only - Instant)"
echo ""

read -p "Enter choice (1-3): " choice

case $choice in
    1)
        echo "🚀 Render Deployment Steps:"
        echo "=========================="
        echo ""
        echo "1. Go to https://render.com"
        echo "2. Sign up with email"
        echo "3. Click 'New +' → 'Web Service'"
        echo "4. Connect GitHub or upload code"
        echo "5. Configure:"
        echo "   Build Command: pip install -r backend/requirements-prod.txt"
        echo "   Start Command: cd backend && uvicorn main:app --host 0.0.0.0 --port \$PORT"
        echo "6. Deploy!"
        echo ""
        echo "Your backend URL will be: https://your-app-name.onrender.com"
        echo "API docs: https://your-app-name.onrender.com/docs"
        ;;
    2)
        echo "🚂 Railway + Vercel Deployment Steps:"
        echo "=================================="
        echo ""
        echo "1. Create GitHub repository at https://github.com/new"
        echo "2. Push your code:"
        echo "   git remote add origin https://github.com/yourusername/your-repo.git"
        echo "   git push -u origin master"
        echo "3. Deploy backend to Railway:"
        echo "   - Go to https://railway.app"
        echo "   - Connect GitHub repo"
        echo "   - Deploy automatically"
        echo "4. Deploy frontend to Vercel:"
        echo "   - Go to https://vercel.com"
        echo "   - Connect GitHub repo"
        echo "   - Deploy automatically"
        echo ""
        echo "Your URLs will be:"
        echo "Backend: https://your-app.railway.app"
        echo "Frontend: https://your-app.vercel.app"
        ;;
    3)
        echo "⚡ Netlify Quick Deploy (Frontend Only):"
        echo "======================================"
        echo ""
        echo "1. Build your frontend:"
        echo "   cd frontend && npm run build"
        echo "2. Go to https://netlify.com"
        echo "3. Drag and drop the 'dist' folder"
        echo "4. Get instant URL!"
        echo ""
        echo "Your frontend URL will be: https://random-name.netlify.app"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac

echo ""
echo "🎉 After deployment, you'll have public URLs to access your app!"
echo "📱 Test your app by uploading an audio file"
echo "🔧 Check API docs at your-backend-url/docs"
