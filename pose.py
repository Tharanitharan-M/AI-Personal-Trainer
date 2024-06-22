import cv2
import mediapipe as mp
import math


class Posedetector():

    def __init__(self, mode=False, complexity=1, smooth=True, enab_seg=False, smooth_seg=True, det_conf=0.5,
                 track_conf=0.5):

        self.static_image_mode = mode
        self.model_complexity = complexity
        self.smoooth_landmarks = smooth
        self.enable_segmentation = enab_seg
        self.smooth_segmentation = smooth_seg
        self.min_detection_confidence = det_conf
        self.min_tracking_confidence = track_conf

        self.mpPose = mp.solutions.pose
        self.mpDraw = mp.solutions.drawing_utils

        self.pose = self.mpPose.Pose(self.static_image_mode,
                                     self.model_complexity,
                                     self.smoooth_landmarks,
                                     self.enable_segmentation,
                                     self.smooth_segmentation,
                                     self.min_detection_confidence,
                                     self.min_tracking_confidence)

    def find_pose(self, img, draw=True):

        imgRBG = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.pose.process(imgRBG)

        if self.results.pose_landmarks and draw:
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def find_position(self, img):

        self.lmList = []
        if self.results.pose_landmarks:  # cannot invoke get_position method without find_pose....

            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])

        return self.lmList

    def find_angle(self, img, p1, p2, p3, draw=True):

        # p2 should be the point with the angle!!!!

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        l_12 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        l_13 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        l_23 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

        angle = math.degrees(math.acos((l_12 ** 2 + l_23 ** 2 - l_13 ** 2) / (2 * l_12 * l_23)))

        cv2.circle(img, (x1, y1), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x3, y3), 5, (255, 0, 0), cv2.FILLED)

        if draw:
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 - 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        return angle
