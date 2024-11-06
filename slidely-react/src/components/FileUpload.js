import React, { useState } from "react";

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    if (selectedFile) {
      // Here you would typically send the file to your backend
      console.log("File selected:", selectedFile.name);
      // Add your file upload logic here
    } else {
      console.log("No file selected");
    }
  };

  return (
    <div>
      <h2>Upload PDF or TXT File</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} accept=".pdf,.txt" />
        <button type="submit">Upload</button>
      </form>
      {selectedFile && <p>Selected file: {selectedFile.name}</p>}
    </div>
  );
};

export default FileUpload;
