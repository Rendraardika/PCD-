import cv2

img = cv2.imread("Fig0335(a)(ckt_board_saltpep_prob_pt05).tif")
k_size_3 = 3
k_size_5 = 5

median_img =cv2.  medianBlur(img, k_size_3)
median_img = cv2.medianBlur(median_img, k_size_5)

cv2.imshow("original", img)
cv2.imshow("Median", median_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
