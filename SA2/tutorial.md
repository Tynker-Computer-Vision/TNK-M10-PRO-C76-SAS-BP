Process the Video
==================

In this activity, you will learn to preprocess the detected face in real time video.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/2071954/images/10572927/Slide_7_P2.gif" width = "480" height = "220">


Follow the given steps to complete this activity:

1. Preprocess the video

* Open the main.py file.

* Crop the face from the image  and store the image in `croppedImg` variable.

    `croppedImg = img[Y:Y+H, X:X+W]`

* Resize the croppedImg to `300*300` and store it in `resizedImg`.

    `resizedImg = cv2.resize(croppedImg, (300, 300))`

* Show resized image.

    `cv2.imshow("ResizedImage", resizedImg)`

* Convert the `resized Img` to `numpy array` so that it can be feeded to the AI model.

    `resizedImg = np.array([resizedImg])`

* Save and run the code to check the output.

