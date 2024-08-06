import cv2
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "../resources", "piece.png")

img = cv2.imread(img_path, cv2.IMREAD_COLOR)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()