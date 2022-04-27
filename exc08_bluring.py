import cv2
import numpy as np

"""
correlation     -> G = h ⨂ F
convolution     -> G = h * F
    G = input image yg dihasilkan 
    h = kernel / filter
    F = input imagenya

cv2.blur(img, ksize, anchor)
ksize adalah kernel size, semakin tinggi kernelnya semakin ngeblur, semakin rendah semakin kontras. (x,y) x = horizontal, y = vertical
anchor adalah lokasi titik pixel yg dievaluasi terhadap neoghbournya, jika negative maka titiknya berada di pusat kernel

cv2.GaussianBlur(img, ksize, sigmaX, sigmaY)                    -> saya singkat menjadi gblur untuk naming 
sigmaX standar deviasi untuk x, dihitung menggunakan kernel size
sigmaY standar deviasi untuk y, dihitung menggunakan kernel size

"""

img = cv2.imread("gambar/mriscan.jpg")
title_window_blur = 'Blur biasa'
title_window_gblur = 'Gaussian blur'
title_window_blurgabungan = 'Blur biasa & Gaussian blur'
h, w, c = img.shape
kernel_max = 10
kernel_default = 3


def blurBiasa():
    image_blur_verti = cv2.blur(img, (1, 7), (-1, -1))
    image_blur_hori = cv2.blur(img, (7, 1), (-1, -1))
    cv2.imshow('Gambar asli', img)
    cv2.imshow('Gambar blur vertical', image_blur_verti)
    cv2.imshow('Gambar blur horizontal', image_blur_hori)
    cv2.namedWindow(title_window_blur)
    cv2.createTrackbar('kernel', title_window_blur, kernel_default, kernel_max, fungsi_trackbar_blur)
    fungsi_trackbar_blur(kernel_default)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar_blur(val):
    if val > 0:
        blur = cv2.blur(img, (val, val), (-1, -1))
        cv2.imshow(title_window_blur, blur)


def gaussianBlur():
    gblur = cv2.GaussianBlur(img, (3, 3), 0, 0)
    cv2.imshow('Gambar asli', img)
    cv2.imshow('Gambar gaussian blur ', gblur)
    cv2.namedWindow(title_window_gblur)
    cv2.createTrackbar('kernel', title_window_gblur,kernel_default, kernel_max, fungsi_trackbar_gblur)
    fungsi_trackbar_gblur(kernel_default)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar_gblur(val):
    if val > 0 and val % 2 == 1:                                                            # kernelsize dibawah ini diset agar selalu ganjil
        blur = cv2.GaussianBlur(img, (val, val), 0, 0)
        cv2.imshow(title_window_gblur, blur)


def blurGabungan():
    cv2.namedWindow(title_window_blurgabungan)
    cv2.createTrackbar('kernel', title_window_blurgabungan,kernel_default, kernel_max, fungsi_trackbar_blur_gblur)
    fungsi_trackbar_blur_gblur(kernel_default)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar_blur_gblur(val):
    if val > 0 and val % 2 == 1:
        blur = cv2.blur(img, (val, val), (-1, -1))
        gblur = cv2.GaussianBlur(img, (val, val), 0, 0)
        frame = np.zeros((h, w*2, c)).astype(np.uint8)
        frame[0:h, 0:w] = blur                                                              # membuat frame untuk blur biasa
        frame[0:h, w:2*w] = gblur                                                           # membuat frame untuk gaussian blur
        cv2.imshow(title_window_blurgabungan, frame)


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. blur secara halus\n2. blur secara halus dengan gaussian blur\n3. blur biasa & gaussian blur\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            blurBiasa()  

        elif inputan == '2':
            gaussianBlur()

        elif inputan == '3':
            blurGabungan()

        else:
            break