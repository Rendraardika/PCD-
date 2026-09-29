import cv2
import numpy as np

img = cv2.imread("Fig0316(4)(bottom_left).tif", 0)

hasil = np.zeros_like(img)

for y in range(1, img.shape[0] - 1):
    for x in range(1, img.shape[1] - 1):

        window = img[y-1:y+2, x-1:x+2]

        hist = np.bincount(window.ravel(), minlength=256)
        cdf = np.cumsum(hist) / window.size

        hasil[y, x] = round(255 * cdf[img[y, x]])

cv2.imshow("Original", img)
cv2.imshow("Local HE", hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()