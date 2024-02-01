import cv2
import mediapipe as mp
import time

cTime =0
pTime=0

cap=cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw= mp.solutions.drawing_utils
while True :
    success , img = cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks :
        for handlmks in results.multi_hand_landmarks:
            for index , landmark in enumerate(handlmks.landmark) :
                height , width , channel =img.shape
                posX , posY  = int(landmark.x*width) , int(landmark.y*height)
                print(id ,posX,posY)
                if index==4:
                    cv2.circle(img,(posX,posY) , 15,(0,255,255),cv2.FILLED)

            mpDraw.draw_landmarks(img,handlmks,mpHands.HAND_CONNECTIONS)


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    text="fps : "+str(int(fps))
    cv2.putText(img,text,(10,70),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)
    cv2.imshow("img",img)
    cv2.waitKey(1)
