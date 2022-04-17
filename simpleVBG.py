import cv2 as cv
from cvzone.SelfiSegmentationModule import SelfiSegmentation
#install 'pip install opencv-python cvzone mediapipe'

cap = cv.VideoCapture(0)
segment = SelfiSegmentation()
bg = cv.imread('bg.jpg') #direktori foto background, ukuran harus sama dengan resolusi

while True:
    _, img = cap.read()
    img1 = segment.removeBG(img, bg, threshold=0.7)
    cv.imshow("ori", img)
    cv.imshow("hasil", img1)
    if cv.waitKey(10) == 27:
        break
