import cv2
import numpy as np

img = cv2.imread("Fig0305(a)(DFT_no_log).tif")

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_abs = cv2.convertScaleAbs(laplacian)

cv2.imshow("original", img)
cv2.imshow("laplacian", laplacian_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()