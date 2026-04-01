from flask import Flask, request, jsonify
from chatbot import intent  # Make sure this function is correctly defined in chatbot.py
from sorter import read  # Ensure this function is in sorter.py and works as expected
import cohere
import os
import random
from flask_cors import CORS

app = Flask(__name__)  # No need to specify static_folder if it's the default 'static'
CORS(app)

# Initialize Cohere client
co = cohere.Client(os.environ.get('COHERE_API_KEY'))

# Function to get matching images based on intent
def get_matching_images(intent_result, emotion_data, limit=2):
    mood, setting = intent_result.split()  # Split intent result into mood and setting
    face_count = 'single' if setting == 'individual' else 'multiple'
    
    # Retrieve all matching images
    images = [img for img in emotion_data.get(mood, {}).get(face_count, [])]
    
    # Shuffle the images to randomize
    random.shuffle(images)
    
    # Return the specified number of images
    return images[:limit]

# Read and process images from the folder
folder_path = os.environ.get('IMAGES_FOLDER_PATH')
emotion_data = read(folder_path)

# Flask route to handle image retrieval based on user input
@app.route('/api/images', methods=['POST'])
def get_images():
    data = request.json
    user_input = data['user_input']
    intent_result = intent(user_input)
    matching_images = get_matching_images(intent_result, emotion_data)
    
    # Generate image paths for the frontend
    image_paths = [os.path.join('/static/images', img.filename) for img in matching_images]
    
    return jsonify(image_paths=image_paths)

# Serve React App if you have a build folder for React
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=False)