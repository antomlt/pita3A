import cv2 as cv
dirCascadeFiles = r'../opencv/haarcascades_cuda/'

# Get files from openCV : https://github.com/opencv/opencv/tree/3.4/data/haarcascades
classCascadefacial = cv.CascadeClassifier( "haarcascade_frontalface_default.xml")
 
def facialDetectionAndMark(_image, _classCascade):
    imgreturn = _image.copy()
    gray = cv.cvtColor(imgreturn, cv.COLOR_BGR2GRAY)
    faces = _classCascade.detectMultiScale(
        gray,
        scaleFactor=2,
        minNeighbors=5,
        minSize=(10, 10),
        flags = cv.CASCADE_SCALE_IMAGE
    )
    for (x, y, w, h) in faces:
        cv.rectangle(imgreturn, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return imgreturn

