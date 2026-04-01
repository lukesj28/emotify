# Emotify

A mental health app that surfaces old memories based on your current mood. Tell Emotify how you're feeling, and it retrieves photos from your local library that match — or counteract — that emotion.

Built at UofT Hacks. Integrates Auth0, Cohere, and DeepFace.

---

## How It Works

1. **Index your photos** — The backend scans your local photo library using DeepFace to detect emotions and count people in each image. This metadata is stored in a local database.
2. **Tell it how you feel** — Type a prompt in the chatbot (e.g., "I'm sad" or "show me two happy people"). Cohere classifies your input into an emotion and optional filters.
3. **Get your memories** — The app queries the indexed database and returns matching photos. If you're feeling down, it deliberately surfaces happy group photos to cheer you up.

---

## Setup

### Prerequisites

- Node.js
- Python 3
- A Cohere API key
- An Auth0 account

### Backend

```bash
cd backend
pip install deepface cohere opencv-python
```

Run the image indexing pipeline on your photo directory:

```bash
python facialdeepface.py   # Analyze emotions in photos
python merge.py            # Build the local database
```

Start the chatbot server:

```bash
python chatbot.py
```

### Frontend

```bash
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## Example Queries

| Input | Result |
|---|---|
| "I'm sad" | Sad photos |
| "I'm happy" | Happy photos and video clips |
| "show me two happy people" | Photos with exactly two people both tagged as happy |
