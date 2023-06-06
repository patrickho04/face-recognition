import os

import cv2  # for cam

cap = cv2.VideoCapture(0)               # open cam
cap.set(3, 640)                         # x pixels
cap.set(4, 480)                         # y pixels

imgBackground = cv2.imread('Resources/background.png')

# Importing mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)                                   # gets name of all images in folderModePath
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))       # creates link to imgs in Resources
# print(len(imgModeList))       # 4

# UI
while True:
    # cam on
    success, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img                 # setting pixels on imgBackground to cam for overlay
    imgBackground[44:44+633, 808:808+414] = imgModeList[1]      # mode overlay (3:active 2:marked  1:student data  0:already marked)
    # cv2.imshow("Webcam", img)

    # graphics
    cv2.imshow("Face Attendance", imgBackground)


    cv2.waitKey(1)
