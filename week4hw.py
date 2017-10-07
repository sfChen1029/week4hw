import cv2
import numpy as np

fileLocation = "320px-Flag_of_Japan.svg.png" # name of location
orig_img = cv2.imread(fileLocation)

#cv2.imshow("Japanese flag",orig_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

hsv_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2HSV)
#cv2.imshow("HSV", hsv_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

THRESHOLD_MIN = np.array([1, 0, 0], np.uint8)
THRESHOLD_MAX = np.array([255, 255, 255], np.uint8)

framethreshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)
cv2.imshow("threshed", framethreshed)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
(_, contours, _) = cv2.findContours(framethreshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #what are the different variables

cv2.drawContours(orig_img, contours, -1, (0,255,255),4)
cv2.imshow("final", orig_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
