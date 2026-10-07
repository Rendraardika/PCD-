import cv2
import numpy as np

img = cv2.imread("Fig0314(a)(100-dollars).tif", 0)
k_size_3 = 3
k_size_5 = 5
pad_3 = k_size_3 // 2
pad_5 = k_size_5 // 2

mean_manual_3 = np.zeros_like(img)
mean_manual_5 = np.zeros_like(img)

img_pad_3 = np.pad(img, pad_3, "constant", constant_values=0)
img_pad_5 = np.pad(img, pad_5, "constant", constant_values=0)

tinggi, lebar = img.shape

print("Sedang memproses mean 3x3, tunggu beberapa detik....")

# looping manual untuk menggeser kernel piksel
for y in range(tinggi):
    for x in range(lebar):
        area = img_pad_3[y : y + k_size_3, x : x + k_size_3]
        mean_manual_3[y, x ] = np.mean(area)

print("Sedang memproses mean 5x5, tuggu beberapa detik....")

for y in range(tinggi):
    for x in range(lebar):
        area = img_pad_5[y : y + k_size_5, x : x + k_size_5]
        mean_manual_5[y, x] = np.mean(area)

cv2.imshow("original", img)
cv2.imshow("mean_manual_3", mean_manual_3)
cv2.imshow("mean_manual_5", mean_manual_5)
cv2.waitKey(0)
cv2.destroyAllWindows()