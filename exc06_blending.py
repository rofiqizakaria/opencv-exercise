import cv2
import numpy as np 

image_banner1 = cv2.imread("gambar/glookosa_banner1.jpg")
image_banner2 = cv2.imread("gambar/glookosa_banner2.jpg")
image_strawberry = cv2.imread("gambar/strawberry.jpg")
image_blueberry = cv2.imread("gambar/blueberry.jpg")
image_sharingan = cv2.imread('gambar/sharingan.jpg')
image_mri = cv2.imread('gambar/mriscan.jpg')
alpha_max = 100
alpha_default_value = 50
title_window = 'Blending Gambar'


def blendingGambar():
    alpha = 0.25
    beta = 1.0 - alpha

    # <<<<< 2 gambar memiliki shape yg sama >>>>>
    blending_img_buah = cv2.addWeighted(image_blueberry, alpha, image_strawberry, beta, 0.0)
    blending_img_gloo = cv2.addWeighted(image_banner1, alpha, image_banner2, beta, 0.0)
    cv2.imshow('Hasil blending buah ', blending_img_buah)
    cv2.imshow('Hasil blending glookosa', blending_img_gloo)

    # <<<<< 2 gambar memiliki shape yg beda >>>>>
    h1, w1, c1 = image_sharingan.shape
    image_mri_reshape = cv2.resize(image_mri, (w1, h1))
    blending_img_2shape = cv2.addWeighted(image_sharingan, alpha, image_mri_reshape, beta, 0.0)
    cv2.imshow('Hasil blending sharingan dgn mri scan', blending_img_2shape)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def blendingGambardgnTrackbar():
    cv2.namedWindow(title_window)
    cv2.createTrackbar('alpha', title_window, alpha_default_value, alpha_max, fungsi_trackbar)
    fungsi_trackbar(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar(val):
    alpha = val / alpha_max
    beta = 1.0 - alpha
    blending_img_buah = cv2.addWeighted(image_blueberry, alpha, image_strawberry, beta, 0.0)
    cv2.imshow(title_window, blending_img_buah)


def overlay():
    alpha = 0.4
    overlay = np.zeros((70, 250, 3)).astype(np.uint8)                                       # 70 itu lebar, 250 itu panjang, 3 itu paten karena jumlah layer RGB sendiri ada 3
    overlay[:, :, 0] = 250                                                                  # pewarnaan untuk code B
    overlay[:, :, 1] = 130                                                                  # pewarnaan untuk code G
    overlay[:, :, 2] = 70                                                                   # pewarnaan untuk code R
    h, w, c = overlay.shape
    img_blend = cv2.addWeighted(image_blueberry[10: 10+h, 10:10+w], 1, overlay, alpha, 0.0)
    image_blueberry[10: 10+h, 10:10+w] = img_blend
    cv2.imshow('Gambar overlay', image_blueberry)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. nge-blending gambar\n2. nge-blending gambar dengan trackbar\n3. overlay\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            blendingGambar()

        elif inputan == '2':
            blendingGambardgnTrackbar()

        elif inputan == '3':
            overlay()

        else:
            break