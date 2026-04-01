// src/ImageFetcher.js
import axios from 'axios';

export const fetchImages = async (inputText) => {
  try {
    const response = await axios.post('http://127.0.0.1:5000/api/images', { user_input: inputText });
    return response.data.image_paths; // Return the paths directly
  } catch (error) {
    console.error('Error fetching images:', error);
    throw error; // Throw the error to be caught in the calling component
  }
};