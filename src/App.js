// src/App.js
import React, { useState } from 'react';
import { useAuth0 } from "@auth0/auth0-react";
import './App.css';
import AnimationComponent from './AnimationComponent';
import { fetchImages } from './ImageFetcher';
import LoginButton from "./login";
import LogoutButton from "./logout";
import ImageGallery from "./ImageGallery";

const App = () => {
  const [inputText, setInputText] = useState('');
  const [imageFilenames, setImageFilenames] = useState([]);
  const [error, setError] = useState(null);
  const [isInputFocused, setIsInputFocused] = useState(false);
  const { isAuthenticated } = useAuth0();
  // Removed useEffect as it was not being used for setting animation speed

  const handleFetchImages = async () => {
    setError(null);
    try {
      const images = await fetchImages(inputText);
      const uniqueImages = [...new Set(images)]; // Ensure unique images
      setImageFilenames(uniqueImages.slice(0, 2)); // Store only up to two images
      setInputText(''); // Clear the input field
    } catch (error) {
      console.error('Error fetching images:', error);
      setError('Failed to fetch images');
    }
  };

  return (
    <div className="App">
      <div className="App-logo">Emotify</div>
      <p>Bring back the feeling.</p>
      {!isAuthenticated && (
        <>
          <LoginButton />
        </>
      )}
      {isAuthenticated && (
         <>
          <input 
            type="text" 
            value={inputText} 
            onChange={(e) => setInputText(e.target.value)} 
            placeholder={isInputFocused ? '' : 'Tell us how you feel...'}
            onFocus={() => setIsInputFocused(true)}
            onBlur={() => {
              if (!inputText) {
                setIsInputFocused(false);
              }
          }}
          />
        <button onClick={handleFetchImages}>Get Images</button>
        {error && <p className="error-message">{error}</p>}
          <LogoutButton />
        </>
      )}
      {/* Removed the duplicate image container div */}
      
      <ImageGallery imageFilenames={imageFilenames} /> {/* This component should handle displaying images */}
      <AnimationComponent />
    </div>
  );
};

export default App;