import os
import cv2

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "../resources", "image1.png")
template_path = os.path.join(script_dir, "../resources", "template1.png")

# Read the main image 
image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread(img_path, cv2.IMREAD_COLOR)

template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR',
            'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']
 
print("[INFO] performing template matching...")
result = cv2.matchTemplate(image, template,cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)

# determine the starting and ending (x, y)-coordinates of the
# bounding box
(startX, startY) = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

# draw the bounding box on the image
cv2.rectangle(image_color, (startX, startY), (endX, endY), (255, 0, 0), 3)
# show the output image
cv2.imshow("Output", image_color)
cv2.waitKey(0)