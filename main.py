import cv2
import matplotlib.pyplot as plt

# Görüntüyü gri tonlamalı olarak oku
image = cv2.imread('image.jpg', 0)

# Otsu ile eşikleme yap
_, otsu_thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Sonuçları görselleştir
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.title('Orijinal Görüntü')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Otsu ile Segmentasyon")
plt.imshow(otsu_thresh, cmap='gray')
plt.axis('off')

plt.tight_layout()