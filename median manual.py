import cv2
import numpy as np

img = cv2.imread('Fig0335(a)(ckt_board_saltpep_prob_pt05).tif', 0)
k_size_3 = 3
k_size_5 = 5

pad_size_3 = 3
pad_size_5 = 5

median_manual_3 = np.zeros_like(img)
median_manual_5 = np.zeros_like(img)

img_padded_3 = np.pad(img, pad_size_3, mode='constant', constant_values=0)
img_padded_5 = np.pad(img, pad_size_5, mode='constant', constant_values=0)

tinggi, lebar = img.shape

print("Sedang memproses median filter, mohon tunggu...")

for y in range(tinggi):
    for x in range(lebar):
        area =  img_padded_3[y : y + k_size_3, x : x + k_size_3]
        nilai_median_3 = np.median(area)
        median_manual_3[y, x] = nilai_median_3

for y in range(tinggi):
    for x in range(lebar):
        area = img_padded_5[y : y + k_size_5, x : x + k_size_5]
        nilai_median_5 = np.median(area)
        median_manual_5[y, x] = nilai_median_5


print("Selesai")

cv2.imshow("original", img)
cv2.imshow("Median 3x3", median_manual_3)
cv2.imshow("Median 5x5", median_manual_5) 
cv2.waitKey(0)
cv2.destroyAllWindows()