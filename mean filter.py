import cv2

# membaca gambar
img = cv2.imread("Fig0314(a)(100-dollars).tif")
k_size_3 = 3
k_size_5 = 5

# menggunakan fungsi bawaan cv2.blur
mean_size_3 = cv2.blur(img, (k_size_3, k_size_3))
mean_size_5 = cv2.blur(img, (k_size_5, k_size_5))

# Hasil
cv2.imshow("Original", img)
cv2.imshow("Mean Filter 3 x 3", mean_size_3)
cv2.imshow("Mean Filter 5 x 5", mean_size_5)

cv2.waitKey(0)
cv2.destroyAllWindows()
