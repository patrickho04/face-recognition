import cv2
import face_recognition
import pickle
import os

# Importing face images into a list
folderImgPath = 'Images'
imgPathList = os.listdir(folderImgPath)                                     # gets name of all images in folderModePath
imgList = []
studentIDs = []
for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderImgPath,path)))            # creates list of face images
    # os.path.splitext(path) + splits <name>.jpeg to ('<name>', '.jpeg')
    studentID = os.path.splitext(path)[0]
    studentIDs.append(studentID)


# turns images into readable data so we can detect if face has been seen before
def findEncodings(imageList):
    encodeList = []
    for img in imageList:
        # opencv uses BGR, but face recognition library uses RGB
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]      # match IDs to images
print("Encoding Finished")

# create file to save images
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()
print("File Saved")
