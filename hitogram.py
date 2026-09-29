import cv2
import numpy as np

src = cv2.imread("Fig0316(4)(bottom_left).tif", 0)
ref = cv2.imread("Fig0316(1)(top_left).tif", 0)

if src is None or ref is None:
    print("Gambar tidak ditemukan")
    exit()

hist_src = np.bincount(src.ravel(), minlength=256)
hist_ref = np.bincount(ref.ravel(), minlength=256)

cdf_src = np.cumsum(hist_src) / src.size
cdf_ref = np.cumsum(hist_ref) / ref.size

mapping = np.zeros(256, dtype=np.uint8)

for i in range(256):
    mapping[i] = np.argmin(np.abs(cdf_src[i] - cdf_ref))

hasil = mapping[src]

cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Hasil Matching", hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()