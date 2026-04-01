from deepface import DeepFace
import cv2
import os

def analyze_emotions(image_path):
    try:
        # Read the image using OpenCV
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Image not loaded; ensure the image path is correct.")

        # Analyze the image for emotions with multiple face support
        analysis = DeepFace.analyze(img, actions=['emotion'], enforce_detection=True, detector_backend='mtcnn')
       
        # Extract emotions
        if isinstance(analysis, dict):
            # Single face detected
            return [analysis.get('dominant_emotion', 'No emotion detected')]
        elif isinstance(analysis, list):
            # Multiple faces detected
            return [face.get('dominant_emotion', 'No emotion detected') for face in analysis]
        else:
            return ['Error in analysis result format']

    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return ['Error during analysis']

def analyze_folder(folder_path):
    folder_path = os.path.abspath(folder_path)
    results = {}
    all_emotions = set()  # Set to store all unique emotions found

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            emotions = analyze_emotions(image_path)
            results[filename] = emotions
            all_emotions.update(emotions)

    return results, all_emotions

# Path to the folder containing images
folder_path = os.environ.get('IMAGES_FOLDER_PATH')

# Analyze all images in the folder and get all emotions
folder_results, all_emotions = analyze_folder(folder_path)

# Print results for each image
for image, emotions in folder_results.items():
    print(f"Image: {image}, Detected Emotions: {emotions}")

# Print all unique emotions found
print("\nAll Detected Emotions:", all_emotions)