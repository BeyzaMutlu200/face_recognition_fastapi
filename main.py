import face_recognition
import cv2
import numpy as np 
import os


DATABASE_PATH = "face_dataset"

def load_img(name):
   print(name)
   base_dir="C:\\Users\\Beyza\\g_teknik\\face_recognition\\face_dataset"
   recog_dir=os.path.join(base_dir, name)
   
   loaded_img=face_recognition.load_image_file(recog_dir)
   return loaded_img

def encoding_img(name):
   loaded_img=load_img(name)
   encoded_img=face_recognition.face_encodings(loaded_img)
    
   #this statement have then one more problems, the face cant be found, the image cant be encode, the list is zero.
   if encoded_img == 0:
      exit()   
   return encoded_img[0]


def bring_all_images():
    known_face_names = []
    known_face_encodings = []
    for name in os.listdir(DATABASE_PATH):
        known_face_names.append(name)
        known_face_encodings.append(encoding_img(name))
    print(known_face_names)
    return {"known_face_names": known_face_names, "known_face_encodings":known_face_encodings}

def recognize_person():
    # Take capture from webcam 
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Can't access camera")
        exit()

    print("im here")
    all_img=bring_all_images()
    known_face_encodings=all_img['known_face_encodings']
    known_face_names=all_img['known_face_names']

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        
        # Find the faces in the frame
        frame_locations = face_recognition.face_locations(frame)
        frame_encodings = face_recognition.face_encodings(frame, frame_locations)

        #draw a rectangle around the faces
        for (top, right, bottom, left), frame_encoding in zip(frame_locations, frame_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, frame_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow("Video", frame)

        if cv2.waitKey(30) == 27 :
            break

    cap.release()
    cv2.destroyAllWindows()
