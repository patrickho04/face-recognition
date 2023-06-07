import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import db
from firebase_admin import storage
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://attendance-system-5a6cb-default-rtdb.firebaseio.com/',
    'storageBucket': 'attendance-system-5a6cb.appspot.com'
})

# Importing face images into a list
folderImgPath = 'Images'
imgPathList = os.listdir(folderImgPath)                                     # gets name of all images in folderModePath
imgList = []
studentIDs = []
for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderImgPath,path)))            # creates list of face images
    # os.path.splitext(path) + splits <name>.jpeg to ('<name>', '.jpeg')

    # send images to Firebase storage
    fileName = f'{folderImgPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # make list of student IDs
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
