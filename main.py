import cv2  # for cam

cap = cv2.VideoCapture(0)               # open cam
cap.set(3, 640)                         # x pixels
cap.set(4, 480)                         # y pixels

imgBackground = cv2.imread('Resources/background.png')



while True:
    # cam on
    success, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img         # setting pixels on imgBackground to cam for overlay
    # cv2.imshow("Webcam", img)

    # graphics
    cv2.imshow("Face Attendance", imgBackground)


    cv2.waitKey(1)
