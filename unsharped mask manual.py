import cv2
import numpy as np

# Baca gambar
img = cv2.imread("Fig0335(a)(ckt_board_saltpep_prob_pt05).tif", 0)

# membuat versi blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# ubah ke float agar perhitungan tidak eror
img_float = img.astype(np.float32)
blur_float = blurred.astype(np.float32)

# membuat mask
mask = img_float - blur_float

# Menentukan bobot (unsharp, standart k=1)
k_1 = 1.0
k_3 = 3.0
unsharp_manual_1 = img_float + (k_1 * mask)
unsharp_manual_3 = img_float + (k_3 * mask)

# membatasi nilai
unsharp_manual_1 = np.clip(unsharp_manual_1, 0, 255)
unsharp_manual_1 = unsharp_manual_1.astype(np.uint8)

unsharp_manual_3 = np.clip(unsharp_manual_3, 0, 255)
unsharp_manual_3 = unsharp_manual_3.astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("unsharped K = 1", unsharp_manual_1)
cv2.imshow("unsharped K = 3", unsharp_manual_3)
cv2.waitKey(0)
cv2.destroyAllWindows()