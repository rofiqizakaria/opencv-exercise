import cv2
import numpy as np

"""
image binarization adalah proses membuat gambar menjadi hitam putih hanya dengan memiliki nilai pixel antara 0 s/d 255
cv2.threshold(img, threshold_value, max_value, threshold_type)

"""

image_mri = cv2.imread("gambar/mriscan.jpg")
title_window_binarization = 'ini image binary dalam satu frame'
biner_max = 255
biner_default = 127
img = cv2.imread("gambar/sharingan.jpg")
h, w, c = img.shape


def binarisasiGambar():
    cv2.namedWindow(title_window_binarization)
    cv2.createTrackbar('threshold', title_window_binarization, biner_default, biner_max, fungsi_trackbar_binarisasi)
    fungsi_trackbar_binarisasi(biner_default)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar_binarisasi(val):
    ret_biner, img_biner = cv2.threshold(img, val, biner_max, cv2.THRESH_BINARY)
    ret_biner_inv, img_biner_inv = cv2.threshold(img, val, biner_max, cv2.THRESH_BINARY_INV)
    ret_trunc, img_trunc = cv2.threshold(img, val, biner_max, cv2.THRESH_TRUNC)
    ret_tozero, img_tozero = cv2.threshold(img, val, biner_max, cv2.THRESH_TOZERO)
    ret_tozero_inv, img_tozero_inv = cv2.threshold(img, val, biner_max, cv2.THRESH_TOZERO_INV)
    frame = np.zeros((h*2, w*3, c )).astype(np.uint8)
    frame[0:h, 0:w] = img
    frame[0:h, w:2*w] = img_biner
    frame[0:h, 2*w:3*w] = img_biner_inv
    frame[h:2*h, 0:w] = img_trunc
    frame[h:2*h, w:2*w] = img_tozero
    frame[h:2*h, 2*w:3*w] = img_tozero_inv
    cv2.imshow(title_window_binarization, frame)
    

def otsuThresholding():
    gambarX = cv2.cvtColor(image_mri, cv2.COLOR_BGR2GRAY)
    gblurX = cv2.GaussianBlur(gambarX, (5,5), 0)                                            # thresholding otsu seteleh filter gaussian
    ret1, th = cv2.threshold(gambarX, 127, 255, cv2.THRESH_BINARY)                          # thresholding global
    ret2, otsu_th = cv2.threshold(gambarX, 0, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU) # thresholding otsu
    ret3, otsu_th_gblbur = cv2.threshold(gblurX, 0, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    cv2.imshow('Gambar orisinil ', gambarX)
    cv2.imshow('Global thresholding ', th)
    cv2.imshow('Otsu thresholding ', otsu_th)
    cv2.imshow('Otsu thresholding dengan gaussian', otsu_th_gblbur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. membinerisasikan gambar\n2. otsu thresholding\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            binarisasiGambar()

        elif inputan == '2':
            otsuThresholding()

        else:
            break