from cvzone.FaceDetectionModule import FaceDetector
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

detector = FaceDetector()

while True:
    try:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        
        img, bboxs = detector.findFaces(img, draw=False)

        if bboxs: 
            for box in bboxs:
                X, Y, W, H = box['bbox']

                # Crop the face from the image  and store the image in croppedImg
                
                # Resize the croppedImg to 300*300 and store it in resizedImg
                
                # Show resized image
                
                # Convert the resized Img to numpy array so that it can be feeded to the AI model
                

                img = cv2.rectangle(img, (X, Y), (X+W, Y+H), (255, 255, 255), 1)
             
        cv2.imshow("Image", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print("Exception", e)

cv2.destroyAllWindows()
