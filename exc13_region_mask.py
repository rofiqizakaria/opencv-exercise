import cv2
from cv2 import bitwise_not
from cv2 import bitwise_xor
from cv2 import bitwise_or 
import numpy as np 
import math

"""     -> regionMask():
cv2.bitwise_and(img1, img2, mask) # bisa juga pakai bitwise_not, bitwise_xor, bitwise_or
mask itu optional operation (8-bit single channel) 
mengambil region of interest bukan bentuk objek objek non-simetrical / tak beraturan

"""

if __name__ == "__main__":
    img_sharingan = cv2.imread("gambar/sharingan.jpg")
    img_blueberry = cv2.imread("gambar/blueberry.jpg")
    img_blueberry2 = cv2.imread("gambar/blueberry2.jpg")
    imgX = img_blueberry
    h, w, c = imgX.shape
    wx0 = int(w * (1/5))
    hx0 = int(h * (1/5))
    wxt = int(w * (4/5))
    hxt = int(h * (4/5))
    
    xmask = np.zeros((h, w)).astype(np.uint8)
    gray = cv2.cvtColor(img_blueberry2, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(xmask, (wx0,hx0), (wxt,hxt), (255,255,255), -1)
    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # <<<<< dibawah ini merupakan Bitwise menggunakan persegi panjang >>>>>  
    mask_not_box = cv2.bitwise_not(img_blueberry, mask=xmask)
    mask_and_box = cv2.bitwise_and(img_blueberry, img_blueberry2, mask=xmask)
    mask_or_box = cv2.bitwise_or(img_blueberry, img_blueberry2, mask=xmask)
    mask_xor_box = cv2.bitwise_xor(img_blueberry, img_blueberry2, mask=xmask)

    # <<<<< dibawah ini merupakan Bitwise menggunakan thresholding >>>>>
    mask_not_thresh = cv2.bitwise_not(img_blueberry, mask=thresh)
    mask_and_thresh = cv2.bitwise_and(img_blueberry, img_blueberry, mask=thresh)
    mask_or_thresh = cv2.bitwise_or(img_blueberry2, img_blueberry, mask=thresh)
    mask_xor_thresh = cv2.bitwise_xor(img_blueberry2, img_blueberry, mask=thresh)

    cv2.imshow('Gambar orisinil', imgX)
    cv2.imshow('box template', xmask)
    cv2.imshow("mask 'bitsiwe_and' box", mask_and_box)
    cv2.imshow("mask 'bitwise_not' box", mask_not_box)
    cv2.imshow("mask 'bitwise_or' box", mask_or_box)
    cv2.imshow("mask 'bitwise_xor' box", mask_xor_box)
    cv2.imshow("thresh template", thresh)
    cv2.imshow("mask 'bitwise_and' thresh", mask_and_thresh)
    cv2.imshow("mask 'bitwise_not' thresh", mask_not_thresh)
    cv2.imshow("mask 'bitwise_or' thresh", mask_or_thresh)
    cv2.imshow("mask 'bitwise_xor' thresh", mask_xor_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






