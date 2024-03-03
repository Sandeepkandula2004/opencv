import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

keyboard = Controller()

hands = HandDetector(detectionCon=0.8, maxHands=2)

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    
    allhands, img = hands.findHands(img=img, draw=False, flipType=True)
    
    if allhands:

        for myhand in allhands:

            count = hands.fingersUp(myHand=myhand)
            if myhand['type'] == 'Left':
                if count.count(1) == 5:
                    keyboard.release(Key.left)
                else:
                    keyboard.press(Key.left)

            if myhand['type'] == 'Right':
                if count.count(1) == 0:
                    keyboard.press(Key.right)
                else:
                    keyboard.release(Key.right)
                    
         

    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

