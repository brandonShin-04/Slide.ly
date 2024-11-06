import React from "react";
import Navbar from "./components/navbar";
import FileUpload from "./components/FileUpload";

function App() {
  return (
    <div>
      <div>
        <Navbar />
      </div>
      <div>
        <h1>Upload File Here</h1>
        <FileUpload />
      </div>
    </div>
  );
}

export default App;
