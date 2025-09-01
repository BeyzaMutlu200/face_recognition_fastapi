# Face Recognition FastAPI

This repository contains a **real-time face recognition system using a webcam** and a **FastAPI-based face data upload API**. Face recognition is implemented using `face_recognition` and `OpenCV`, and new face data can be added via API.

## Features

- Real-time face recognition via webcam (`main.py`)
- Add new face images through API (`api_try.py`)
- Display recognized faces with names
- Handle error scenarios

## Requirements

- Python >= 3.8
- OpenCV (`opencv-python`)
- face_recognition
- numpy
- fastapi
- uvicorn

```bash
pip install opencv-python face_recognition numpy fastapi uvicorn
```
## Usage

# Real-Time Face Recognition (main.py)

```bash   
python main.py
```
Recognizes faces stored in the face_dataset folder.
Draws a red rectangle around recognized faces with their names.
Press ESC to exit.

#2.FastAPI: Upload and Recognize Faces (api_try.py)
# Start the API
```bash
python api_try.py

# Or use uvicorn
uvicorn api_try:app --reload
```
# Endpoints

POST /upload_file/
Upload a new face image.

Parameters: name (file name), file (UploadFile)

# Example:
```bash
curl -X POST http://127.0.0.1:8000/upload_file/ -F "name=example.jpg" -F "file=@example.jpg"
```
POST /recog_persons/
Start face recognition via webcam.

# Example:
``` bash
curl -X POST http://127.0.0.1:8000/recog_persons/
```
## File Structure
face_recognition_fastapi/
│
├─ main.py          # Real-time webcam face recognition
├─ api_try.py       # FastAPI for uploading and recognizing faces
├─ face_dataset/    # Folder containing face images
└─ README.md

## Notes

main.py detects faces in real-time from the webcam and displays their names.

api_try.py allows adding new face images via API and starting the recognition process.

Unrecognized faces will be labeled as Unknown.



