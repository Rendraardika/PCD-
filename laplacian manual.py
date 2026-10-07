import cv2
import numpy as np

# baca gambar
img = cv2.imread("Fig0305(a)(DFT_no_log).tif", 0)

# siapkan kernel
kernel_laplacian = np.array([[0,1,0],
                            [1,-4,1],
                            [0,1,0]], dtype = np.float32)
# kanvas kosong
laplacian_manual = np.zeros_like(img, dtype=np.float32)

# kernel size dan padding size
k_size_3 = 3
pad_size_3 = 3 // 2

# menambahkan padding pada gambar
img_padded = np.pad(img, pad_size_3, mode="constant", constant_values=0)
tinggi, lebar = img.shape

print("Sedang memproses Laplacian filter 3x3, mohon tunggu....")

# looping konvolusi
for y in range(tinggi):
    for x in range(lebar):
        area = img_padded[y: y + k_size_3, x: x + k_size_3]

        hasil_hitung = np.sum(area * kernel_laplacian)

        laplacian_manual[y, x] = hasil_hitung

# Penanganan nilai minus (ubah semua angka minus menjadi positif)
laplacian_manual = np.abs(laplacian_manual)

# membatasi nilai agar tidak lebih dari 255
laplacian_manual = np.clip(laplacian_manual, 0, 255)

laplacian_manual = laplacian_manual.astype(np.uint8)

print("selesai!")

# menampilkan gambar asli dan hasil
cv2.imshow("original", img)
cv2.imshow("laplacian", laplacian_manual)
cv2.waitKey(0)
cv2.destroyAllWindows()