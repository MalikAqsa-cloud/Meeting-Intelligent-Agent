import React, { useRef } from 'react';

const FileUpload = ({ onFileUpload, disabled }) => {
  const fileInputRef = useRef(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      onFileUpload(file);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      onFileUpload(file);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  const openFileDialog = () => {
    fileInputRef.current?.click();
  };

  return (
    <div className="w-full">
      <div
        className={`border-2 border-dashed rounded-lg p-8 text-center transition-colors ${
          disabled
            ? 'border-gray-300 bg-gray-100 cursor-not-allowed'
            : 'border-gray-400 hover:border-blue-500 hover:bg-blue-50 cursor-pointer'
        }`}
        onDrop={handleDrop}
        onDragOver={handleDragOver}
        onClick={disabled ? undefined : openFileDialog}
      >
        <div className="space-y-4">
          <div className="mx-auto w-16 h-16 text-gray-400">
            <svg
              className="w-full h-full"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
              />
            </svg>
          </div>
          
          <div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">
              Upload Meeting Audio
            </h3>
            <p className="text-gray-600 mb-4">
              Drag and drop your audio file here, or click to browse
            </p>
            <p className="text-sm text-gray-500">
              Supported formats: MP3, WAV, M4A, FLAC
            </p>
          </div>

          <button
            type="button"
            disabled={disabled}
            className={`px-6 py-2 rounded-lg font-medium transition-colors ${
              disabled
                ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                : 'bg-blue-600 text-white hover:bg-blue-700'
            }`}
          >
            {disabled ? 'Processing...' : 'Choose File'}
          </button>
        </div>
      </div>

      <input
        ref={fileInputRef}
        type="file"
        accept=".mp3,.wav,.m4a,.flac"
        onChange={handleFileChange}
        className="hidden"
        disabled={disabled}
      />
    </div>
  );
};

export default FileUpload;
