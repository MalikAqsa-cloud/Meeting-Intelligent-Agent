import React, { useState } from 'react';

const TranscriptDisplay = ({ transcript }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  if (!transcript) return null;

  const displayText = isExpanded ? transcript : transcript.substring(0, 500) + '...';

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-bold text-gray-900 flex items-center">
          <svg className="w-6 h-6 mr-2 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          Meeting Transcript
        </h2>
        {transcript.length > 500 && (
          <button
            onClick={() => setIsExpanded(!isExpanded)}
            className="text-blue-600 hover:text-blue-800 font-medium"
          >
            {isExpanded ? 'Show Less' : 'Show More'}
          </button>
        )}
      </div>
      
      <div className="bg-gray-50 rounded-lg p-4">
        <p className="text-gray-800 leading-relaxed whitespace-pre-wrap">
          {displayText}
        </p>
      </div>
      
      <div className="mt-4 text-sm text-gray-500">
        {transcript.length} characters
      </div>
    </div>
  );
};

export default TranscriptDisplay;
