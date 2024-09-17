import React, { useState } from 'react';
import { uploadFile } from '../services/api';

interface FileUploadProps {
  onFileUploaded: (fileInfo: { name: string, url: string }) => void;
}

const FileUpload: React.FC<FileUploadProps> = ({ onFileUploaded }) => {
  const [isUploading, setIsUploading] = useState(false);

  const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    setIsUploading(true);

    try {
      const uploadedFileInfo = await uploadFile(file);
      onFileUploaded(uploadedFileInfo);
    } catch (error) {
      console.error('Error uploading file:', error);
      // TODO: Add proper error handling
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="file-upload">
      <input
        type="file"
        onChange={handleFileChange}
        disabled={isUploading}
        style={{ display: 'none' }}
        id="file-input"
      />
      <label htmlFor="file-input" className="file-upload-button">
        {isUploading ? 'Uploading...' : 'Upload File'}
      </label>
    </div>
  );
};

export default FileUpload;