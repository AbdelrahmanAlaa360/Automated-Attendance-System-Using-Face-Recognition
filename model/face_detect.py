import face_recognition
import cv2
import numpy as np
import time
import random
from train_model import train_on_dataset
start = time.time()

#train = input("\nEnter yes to train on dataset otherwise enter no\n")
train = 0
if(train == 1):
    train_on_dataset()
video_capture = cv2.VideoCapture(1)

known_face_encodings = np.load("face_encodings_numpy.npy")
known_face_names = np.load("names_numpy.npy")
print(known_face_encodings)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Get the number of frames in the video
num_frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
num_frames = int(num_frames)
# Set the frame rate to 2 frames per second
frame_rate = 2
names = set()
capturedFrames = set()
cnt=0
now = time.time()
video_duration = 10
future = now + video_duration
exist = True
while(time.time() < future):
    # Get a single frame of video
    ret, frame = video_capture.read()
    if frame is None:
        break
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            names.add(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        if name not in capturedFrames :
            #tempFrame = frame[top:left, bottom-35:right]
            tempFrame = frame[top:bottom, left:right]
            # Save frame to retrain model
            cv2.imwrite("D:\Projects\Automated-Attendance-System-Using-Face-Recognition\media\profile_pics\%s\%s.jpg" % (name, int(time.time())), tempFrame)
            capturedFrames.add(name)
            print(top, left, right, bottom)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cnt += 1
    video_capture.grab()

# Release the webcam
video_capture.release()
cv2.destroyAllWindows()

print("Total Frames = ", num_frames)
print("Covered Frames = ", cnt)
print(names)
end = time.time()
time_taken = int(end - start)

print("Program execution time = ", time_taken, "Sec")
with open('attendance.txt', 'w') as file:
    names_str='\n'.join(names)
    file.truncate()
    file.write(names_str)

print(names)
print(type(names))
end = time.time()
time_taken = int(end - start)