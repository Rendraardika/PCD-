import cv2

img = cv2.imread("laut.jpeg")

ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])

hasil = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow("Original", img)
cv2.imshow("Color HE", hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()