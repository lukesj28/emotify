import React from 'react';
import './ImageGallery.css'; // Make sure to import the CSS file

const ImageGallery = ({ imageFilenames }) => {
  return (
    <div className="gallery">
      {imageFilenames.slice(0, 2).map((filename, index) => ( // Only take the first two images
        <div key={index} className="image-frame">
          <img src={`http://127.0.0.1:5000${filename}`} alt={`User Requested ${index}`} className="gallery-image" />
        </div>
      ))}
    </div>
  );
};

export default ImageGallery;