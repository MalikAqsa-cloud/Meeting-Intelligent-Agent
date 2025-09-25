import React from 'react';

const SummaryDisplay = ({ summary }) => {
  if (!summary) return null;

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
        <svg className="w-6 h-6 mr-2 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        Meeting Summary
      </h2>
      
      <div className="bg-green-50 rounded-lg p-4 border-l-4 border-green-400">
        <p className="text-gray-800 leading-relaxed">
          {summary}
        </p>
      </div>
    </div>
  );
};

export default SummaryDisplay;
