import cv2
import numpy as np
import time
import pose as pm

width = 780
height = 650
dim = (width, height)

pTime = 0
dir = 0
count = 0


# Video by Pavel Danilyuk: https://www.pexels.com/video/a-man-doing-biceps-curls-4367577/
cap = cv2.VideoCapture("bicep curls.mp4")

detector = pm.Posedetector()


def bicep_curls(arm='right'):
    global width, height, dim, pTime, dir, count, cap, detector
    flag = True
    while True:
        success, img = cap.read()
        if not success: return
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        img = detector.find_pose(img)
        lmList = detector.find_position(img)

        if len(lmList) != 0:

            if arm == 'right':
                angle = detector.find_angle(img, 12, 14, 16)
            elif arm == 'left':
                angle = detector.find_angle(img, 11, 13, 15)

            per = np.interp(angle, (60, 145), (100, 0))

            if per == 100:
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                if dir == 1:
                    count += 0.5
                    dir = 0

            cv2.putText(img, str(int(count)), (50, 530), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 5)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if flag:
            time.sleep(10)
            flag = False

if __name__ == "__main__":
    bicep_curls()