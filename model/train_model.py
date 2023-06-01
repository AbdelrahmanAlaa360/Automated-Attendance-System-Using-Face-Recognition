import face_recognition
import os
import numpy as np
import glob

def train_on_dataset():
    print("\nTraining model..\n")
    print("==================\n")
    known_face_encodings = []
    known_face_names = []
    images_path = "D:\Projects\Automated-Attendance-System-Using-Face-Recognition\media\profile_pics"
    subfolders = [ f.path for f in os.scandir(images_path) if f.is_dir() ]
    for subfolder in subfolders:
        images_path = glob.glob(subfolder+'/*')
        print(subfolder)

        for img_path in images_path:
            image = face_recognition.load_image_file(img_path)
            face_encoding = face_recognition.face_encodings(image)[0]
            
            # Name Extraction
            folder_name = os.path.dirname(img_path)
            folder_name = os.path.basename(folder_name)
            known_face_encodings.append(face_encoding)
            known_face_names.append(folder_name)

    #print(known_face_encodings)
    known_face_encodings = np.array(known_face_encodings)
    known_face_names = np.array(known_face_names)

    np.save("face_encodings_numpy.npy", known_face_encodings)
    np.save("names_numpy.npy", known_face_names)
    print("\nModel Trained Successfully!\n")
    print("==================\n\n")