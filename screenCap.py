import cv2
import numpy as np
import mediapipe as mp
import math
import pyautogui
import imutils

fingertips = [8,12,16,20]
thumbtip = 4
counter = 0
cam = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()
def detectFist(img,results) :
    global counter
    handLandmarks = results.multi_hand_landmarks
    if(handLandmarks):
        for hl in handLandmarks:
            lmList = []
            for id in hl.landmark:
                lmList.append(id)
            fingerFoldStatus = []
            for fid in fingertips:
                top_x = lmList[fid].x
                top_y = lmList[fid].y
                bottom_x = lmList[fid-2].x
                bottom_y = lmList[fid-2].y
                if(top_x >= bottom_x):
                    fingerFoldStatus.append(1)
                else:
                    fingerFoldStatus.append(0)
            # print(fingerFoldStatus)
            totalFingers = fingerFoldStatus.count(1)
            if totalFingers == 4 :
                counter = counter + 1
                images = pyautogui.screenshot()
                images = cv2.cvtColor(np.array(images),cv2.COLOR_RGB2BGR)
                cv2.imwrite('screenshot'+str(counter)+'.png',images)
                

while True:
    ret, img = cam.read()
    img = cv2.flip(img,1)
    cv2.imshow('camera',img)
    height,width,channels = img.shape
    results = hands.process(img)
    detectFist(img,results)
    if cv2.waitKey(1) == 32 :
        break

