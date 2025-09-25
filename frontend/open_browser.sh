#!/bin/bash

echo "🌐 Opening Meeting Intelligence Agent in browser..."

# Get the absolute path to the HTML file
HTML_FILE="$(pwd)/index.html"

# Try different browsers
if command -v firefox >/dev/null 2>&1; then
    echo "Opening with Firefox..."
    firefox "file://$HTML_FILE" &
elif command -v google-chrome >/dev/null 2>&1; then
    echo "Opening with Chrome..."
    google-chrome "file://$HTML_FILE" &
elif command -v chromium-browser >/dev/null 2>&1; then
    echo "Opening with Chromium..."
    chromium-browser "file://$HTML_FILE" &
elif command -v xdg-open >/dev/null 2>&1; then
    echo "Opening with default browser..."
    xdg-open "file://$HTML_FILE" &
else
    echo "No browser found. Please open the following file manually:"
    echo "$HTML_FILE"
fi

echo "✅ Browser should be opening now!"
echo "📁 File location: $HTML_FILE"
