import cv2
import mediapipe as mp
import numpy as np
mp_drawing=mp.solutions.drawing_utils
mp_pose= mp.solutions.pose

class Workout:
    def __init__(self):
        self.cap = cv2.VideoCapture('bicepsDemo.mp4')
    
    def calculate_angle(self,a,b,c):
        a = np.array(a) # First
        b = np.array(b) # Mid
        c = np.array(c) # End
        
        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)
        
        if angle >180.0:
            angle = 360-angle
            
        return angle 


    def workout_detection(self,number,video):
        counter = 0 
        stage = None
        if number ==1:
            cap = cv2.VideoCapture(video)
            with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    # Recolor image to RGB
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
                
                    # Make detection
                    results = pose.process(image)
                
                    # Recolor back to BGR
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    
                    # Extract landmarks
                    try:
                        landmarks = results.pose_landmarks.landmark                        
                        # Get coordinates for Right arm            
                        shoulder_right = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                        elbow_right = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                        wrist_right = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                        # Calculate angle
                        
                        angle_for_right_arm = self.calculate_angle(shoulder_right, elbow_right, wrist_right)            

                            
                        if angle_for_right_arm > 160 :
                            stage = "down"
                        if angle_for_right_arm < 30 and stage =='down' :
                            stage="up"
                            counter +=1

                                
                    except:
                        pass
                    calories_burnt=counter*0.2
                    cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
                    
                return counter
                