# image_info.py
class ImageFactory:
    def __init__(self, filename, emotions, source_folder):
        self.filename = filename
        self.emotions = emotions
        self.is_single = len(emotions) == 1
        self.source_folder = source_folder


# sorter.py

from facialdeepface import analyze_folder
import os

def read(folder_path):
    folder_results, _ = analyze_folder(folder_path)
    emotion_data = {}

    for image, emotions in folder_results.items():
        image_info = ImageFactory(image, emotions, folder_path)
        for emotion in set(emotions):  # Use a set to avoid duplicates
            if emotion not in emotion_data:
                emotion_data[emotion] = {'single': [], 'multiple': []}
            if image_info.is_single:
                emotion_data[emotion]['single'].append(image_info)
            else:
                emotion_data[emotion]['multiple'].append(image_info)

    return emotion_data

def retrieve_images(emotion, face_count, emotion_data):
    face_type = 'single' if face_count == 'single' else 'multiple'
    if emotion in emotion_data and face_type in emotion_data[emotion]:
        return emotion_data[emotion][face_type]
    return []

# Usage
folder_path = os.environ.get('IMAGES_FOLDER_PATH')
emotion_data = read(folder_path)

# Retrieve and print 'happy' images with a single face
happy_single_images = retrieve_images('happy', 'single', emotion_data)
for image_info in happy_single_images:
    print(f"Image: {image_info.filename}, Folder: {image_info.source_folder}")
print("happy multiple*********************************************************")
# Retrieve and print 'happy' images with multiple faces
happy_multiple_images = retrieve_images('happy', 'multiple', emotion_data)
for image_info in happy_multiple_images:
    print(f"Image: {image_info.filename}, Folder: {image_info.source_folder}")