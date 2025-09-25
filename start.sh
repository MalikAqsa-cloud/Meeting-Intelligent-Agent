#!/bin/bash

echo "�� Starting Meeting Intelligence Agent..."

# Function to check if a port is in use
check_port() {
    lsof -i :$1 > /dev/null 2>&1
}

# Start backend
echo "📡 Starting FastAPI backend..."
cd backend
if check_port 8000; then
    echo "⚠️  Port 8000 is already in use. Backend may already be running."
else
    source venv/bin/activate 2>/dev/null || python -m venv venv && source venv/bin/activate
    pip install -r requirements.txt > /dev/null 2>&1
    uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
    BACKEND_PID=$!
    echo "✅ Backend started on http://localhost:8000 (PID: $BACKEND_PID)"
fi

# Start frontend
echo "🎨 Starting React frontend..."
cd ../frontend
if check_port 5173; then
    echo "⚠️  Port 5173 is already in use. Frontend may already be running."
else
    npm install > /dev/null 2>&1
    npm run dev &
    FRONTEND_PID=$!
    echo "✅ Frontend started on http://localhost:5173 (PID: $FRONTEND_PID)"
fi

echo ""
echo "🎉 Meeting Intelligence Agent is running!"
echo "📱 Frontend: http://localhost:5173"
echo "🔧 Backend API: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for interrupt
trap 'echo ""; echo "🛑 Stopping services..."; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit' INT
wait
