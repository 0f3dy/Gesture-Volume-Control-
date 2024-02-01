import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm
cTime = 0
pTime = 0
cap = cv2.VideoCapture(0)
detector=htm.handDetector()


while True:
    success, img = cap.read()
    img=detector.findHands(img)
    lmkList=detector.findPositions(img)
    if len(lmkList) !=0 :
        print(lmkList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    text = "fps : " + str(int(fps))
    cv2.putText(img, text, (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    cv2.imshow("img", img)
    cv2.waitKey(1)