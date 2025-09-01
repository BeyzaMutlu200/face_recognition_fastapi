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
Usage
1. Real-Time Face Recognition (main.py)
