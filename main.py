import os
import pickle
import cv2  # for cam
import face_recognition
import numpy as np

cap = cv2.VideoCapture(0)               # open cam
cap.set(3, 640)                         # x pixels
cap.set(4, 480)                         # y pixels

imgBackground = cv2.imread('Resources/background.png')

# Importing mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)                                   # gets name of all images in folderModePath
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))       # creates list of images in Resources

# Importing encoding file
print("Loading Encode File...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIDs = pickle.load(file)
file.close()
encodeListKnown, studentIDs = encodeListKnownWithIDs
print("Encode File Loaded")

# UI
while True:
    # cam on
    success, img = cap.read()

    # compress and convert cam image
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # encode cam image
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162:162+480, 55:55+640] = img                 # setting pixels on imgBackground to cam for overlay
    imgBackground[44:44+633, 808:808+414] = imgModeList[1]      # mode overlay (3:active 2:marked  1:student data  0:already marked)

    # search for saved faces
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)          # measures how close face is too image data (lower is more accurate)

        matchIdx = np.argmin(faceDistance)
        if matches[matchIdx]:
            print("Known Face Detected")
            print(studentIDs[matchIdx])

    # Graphics
    cv2.imshow("Face Attendance", imgBackground)


    cv2.waitKey(1)
