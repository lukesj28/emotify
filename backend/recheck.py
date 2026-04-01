import requests

# URL of the Flask endpoint
url = "http://127.0.0.1:5000/api/images"

# Example data to send (modify as per your application's requirements)
data = {
    "user_input": "Enter some text here to test"
}

# Send a POST request
response = requests.post(url, json=data)

# Print the response (which should be JSON with image paths)
print(response.json())