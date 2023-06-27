Capture Video and Detect Faces
===============================

In this activity, you will learn to read the feed and detect faces.


<img src= "https://s3-whjr-curriculum-uploads.whjr.online/8241f76f-20f2-4c6f-99b8-a3b8862088c8.gif" width = "480" height = "220">


Follow the given steps to complete this activity:

1. Read the feed

* Open the main.py file.

* Import `Face Detection, cv2 and NumPy` library .

    `from cvzone.FaceDetectionModule import FaceDetector`

    `import cv2`

    `import numpy as np`

* Capture the web cam video feed.

    `cap = cv2.VideoCapture(0)`

* Create a detector using FaceDetector.

    `detector = FaceDetector()`

 *   Read single image from the captured feed and store it in img variable.

    `success, img = cap.read()`

* Store the flipped video frames using `cv2.flip(img, 1)`.

    `img = cv2.flip(img, 1)`

* Use detector to find faces in the image and store it in bboxs variable.

    `img, bboxs = detector.findFaces(img, draw=False)`

* Check if `bboxs` exits.

    `if bboxs:`

* Traverse throught each `box` in the `bboxs` using for loop.

    `for box in bboxs:`

* Get `X, Y, W, H` of the box.

    `X, Y, W, H = box['bbox']`

* Draw the rectangle using `X, Y, W, H` to show rectangle on detected face.

    `img = cv2.rectangle(img, (X, Y), (X+W, Y+H), (255, 255, 255), 1)`

* Display the image.    

    `cv2.imshow("Image", img)`x 
         
* Save and run the code to check the output.

