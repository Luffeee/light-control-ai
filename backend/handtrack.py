import cv2
from cvzone.HandTrackingModule import HandDetector
import requests

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.6, maxHands=1)

def is_hand_open(hand):
    fingers = []
    lmList = hand["lmList"]
    handType = hand["type"]

    # Thumb
    if handType == "Left":
        if lmList[4][0] < lmList[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)
    else:  # Right hand
        if lmList[4][0] > lmList[3][0]:
            fingers.append(1)
        else:
            fingers.append(0)

    # Other fingers
    for tipId in [8, 12, 16, 20]:
        if lmList[tipId][1] < lmList[tipId - 2][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1) == 5

while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)

    if hands:
        for hand in hands:
            bbox = hand["bbox"]  
            if is_hand_open(hand):
                cv2.putText(img, "Hand Open", (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                req = requests.get("http://192.168.0.104:8000/led?state=on")
                print(req.content)
            else:
                cv2.putText(img, "Hand Closed", (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                req = requests.get("http://192.168.0.104:8000/led?state=off")
                print(req.content)

    cv2.imshow("Smart Camera", img)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
