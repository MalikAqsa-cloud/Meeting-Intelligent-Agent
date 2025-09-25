import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import TranscriptDisplay from './components/TranscriptDisplay';
import SummaryDisplay from './components/SummaryDisplay';
import ActionItemsDisplay from './components/ActionItemsDisplay';
import LoadingSpinner from './components/LoadingSpinner';
import ErrorMessage from './components/ErrorMessage';

// Get API URL from environment variables
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
  const [isProcessing, setIsProcessing] = useState(false);
  const [isSendingToTrello, setIsSendingToTrello] = useState(false);
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [trelloSuccess, setTrelloSuccess] = useState(null);

  const handleFileUpload = async (file) => {
    setIsProcessing(true);
    setError(null);
    setData(null);
    setTrelloSuccess(null);

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await fetch(`${API_URL}/process-audio`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to process audio');
      }

      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsProcessing(false);
    }
  };

  const handleSendToTrello = async () => {
    if (!data?.action_items?.length) return;

    setIsSendingToTrello(true);
    setTrelloSuccess(null);

    try {
      const response = await fetch(`${API_URL}/send-to-trello`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data.action_items),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to send to Trello');
      }

      const result = await response.json();
      setTrelloSuccess(result.message);
    } catch (err) {
      setError(err.message);
    } finally {
      setIsSendingToTrello(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Meeting Intelligence Agent
          </h1>
          <p className="text-lg text-gray-600">
            Upload your meeting audio to get AI-powered transcription, summary, and action items
          </p>
        </div>

        {/* File Upload Section */}
        <div className="max-w-2xl mx-auto mb-8">
          <FileUpload onFileUpload={handleFileUpload} disabled={isProcessing} />
        </div>

        {/* Loading State */}
        {isProcessing && (
          <div className="max-w-2xl mx-auto mb-8">
            <LoadingSpinner message="Processing your audio file..." />
          </div>
        )}

        {/* Error Display */}
        {error && (
          <div className="max-w-2xl mx-auto mb-8">
            <ErrorMessage message={error} />
          </div>
        )}

        {/* Success Message */}
        {trelloSuccess && (
          <div className="max-w-2xl mx-auto mb-8">
            <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg">
              <div className="flex items-center">
                <svg className="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                {trelloSuccess}
              </div>
            </div>
          </div>
        )}

        {/* Results Display */}
        {data && !isProcessing && (
          <div className="space-y-8">
            {/* Transcript */}
            <TranscriptDisplay transcript={data.transcript} />

            {/* Summary */}
            <SummaryDisplay summary={data.summary} />

            {/* Action Items */}
            <ActionItemsDisplay 
              actionItems={data.action_items}
              onSendToTrello={handleSendToTrello}
              isSendingToTrello={isSendingToTrello}
            />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
