import cv2 
from pyzbar.pyzbar import decode

img= cv2.imread(r"C:\Users\raghv\OneDrive\Desktop\WhatsApp Image 2024-05-08 at 18.50.18_9142c5b9.jpg")

for code in decode(img):
    print(code.data.decode("utf-8"))