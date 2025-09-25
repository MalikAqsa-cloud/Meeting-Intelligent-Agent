import React from 'react';

const ActionItemsDisplay = ({ actionItems, onSendToTrello, isSendingToTrello }) => {
  if (!actionItems || actionItems.length === 0) return null;

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-2xl font-bold text-gray-900 flex items-center">
          <svg className="w-6 h-6 mr-2 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
          </svg>
          Action Items
        </h2>
        
        <button
          onClick={onSendToTrello}
          disabled={isSendingToTrello}
          className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center ${
            isSendingToTrello
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-orange-600 text-white hover:bg-orange-700'
          }`}
        >
          {isSendingToTrello ? (
            <>
              <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-gray-500" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Sending...
            </>
          ) : (
            <>
              <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              Send to Trello
            </>
          )}
        </button>
      </div>
      
      <div className="space-y-3">
        {actionItems.map((item, index) => (
          <div key={index} className="bg-orange-50 rounded-lg p-4 border-l-4 border-orange-400">
            <div className="flex items-start">
              <div className="flex-shrink-0">
                <div className="w-6 h-6 bg-orange-600 text-white rounded-full flex items-center justify-center text-sm font-bold">
                  {index + 1}
                </div>
              </div>
              <div className="ml-3">
                <p className="text-gray-800">{item}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      
      <div className="mt-4 text-sm text-gray-500">
        {actionItems.length} action item{actionItems.length !== 1 ? 's' : ''} found
      </div>
    </div>
  );
};

export default ActionItemsDisplay;
