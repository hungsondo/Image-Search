import cv2
    
# path
path = r'C:\Users\dell\Documents\Image Search\dataset\19.jpg'
    
# Reading an image in default mode
image = cv2.imread(path)
    
# Window name in which image is displayed
window_name = 'Image'
   
(h, w) = image.shape[:2]                 
(cX, cY) = (int(w * 0.5), int(h * 0.5))
  
angle = 0
  
startAngle = 0
  
endAngle = 360
(axesX, axesY) = (int(w * 0.75) // 2, int(h * 0.6) // 2)
# Blue color in BGR
color = (255, 0, 0)
   
# Line thickness of -1 px
thickness = -1
   
# Using cv2.ellipse() method
# Draw a ellipse with blue line borders of thickness of -1 px
image = cv2.ellipse(image, (cX, cY), (axesX, axesY), 90, 0, 360, 255, -1)

# image = cv2.ellipse(image, (cX, cY), (axesX, axesY), angle,
#                           startAngle, endAngle, color, thickness)
# Displaying the image
cv2.imshow(window_name, image) 
cv2.waitKey(0)