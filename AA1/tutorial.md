Change the Color
================

In this activity, you will learn to color the bounding box and age prediction values with different colors.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10580123/image__41_.png" width = "480" height = "220">
<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10580126/image__39_.png" width = "480" height = "220">

Follow the given steps to complete this activity:

1. Add color to text and rectangle

* Open the main.py file.

* Create a `color` variable and assign it RGB values for white color.

    `color = (255, 255, 255)`

* Check if `prediction[0][0]` i.e age is less then `80` and assign a `Magenta/Fuchsia`  color RGB `(255, 0, 255)` to `color` variable.

    `if prediction[0][0] < 80:`

        `color = (255, 0, 255)`

*  Check if `prediction[0][0]` i.e age is less then `40` and assign a `Yellow`  color RGB 
`(255, 255, 0)` to `color` variable.

    `if prediction[0][0] < 60:`

        `color = (255, 255, 0)`


* Check if `prediction[0][0]` i.e age is less then `60` and assign a `Blue`  color RGB 
`(0, 255, 255)` to `color` variable.

    `if prediction[0][0] < 40:`

        `color = (0, 255, 255)`

* Check if `prediction[0][0]` i.e age is less then `20` and assign a `Red`  color RGB 
`(255, 0, 0)` to `color` variable.

    `if prediction[0][0] < 20:`

        `color = (255, 0, 0)`

* Use `color` variable to give color to the `text`.

    `img = cv2.putText(img, str(int(prediction[0][0])), (X, Y), cv2.FONT_HERSHEY_DUPLEX, 1.0, color, 2)`
    
* Use `color` variable to give color to the `rectangle`.

    `img = cv2.rectangle(img, (X, Y), (X+W, Y+H), color, 1)`
                        
* Save and run the code to check the output.

  