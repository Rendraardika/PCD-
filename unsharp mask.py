import cv2

img = cv2.imread("Fig0335(a)(ckt_board_saltpep_prob_pt05).tif", 0)

blurred = cv2.GaussianBlur(img, (5, 5), 0)

unsharped = cv2.addWeighted(img, 2.0, blurred, -1.0, 0)

cv2.imshow("original", img)
cv2.imshow("unsharped", unsharped)
cv2.waitKey(0)
cv2.destroyAllWindows()