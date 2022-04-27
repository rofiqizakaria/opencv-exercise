import cv2 
import numpy as np
import matplotlib.pyplot as plt

"""
memanipulasi gambar berdasarkan bentuk gambar
cv2.dilate(img, kernel, anchor, oterations)
kernel = matrik index nd array, bisa di buat menggunakan np.ones() 
anchor = mengevaluasi nilai kernel pada posisi kernel, default (-1, 1) sebagai posisi tengah kernel / starter point 
iteration = pengulangan action terhadap gambar 

"""

iterate = 1
kernel_size = 3
title_window_dilate = 'Dilasi gambar'
title_window_erode = 'Erosi gambar'
img_dilate = cv2.imread('gambar/sliced_char.png')
gray_dilate = cv2.cvtColor(img_dilate, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_dilate, 127, 255, cv2.THRESH_BINARY)
img_erode = cv2.imread('gambar/mriscan.jpg')
gray_erode = cv2.cvtColor(img_erode, cv2.COLOR_BGR2GRAY)


def pengenalan():
    frame = np.zeros((200,200), np.uint8)
    kernel = np.ones((10,10), np.uint8)                                                     # 10 itu untuk mengatur ketebalan
    cv2.circle(frame, (50,50), 30, (255, 255, 255), -1, cv2.LINE_AA)
    cv2.circle(frame, (140, 140), 30, (255, 255, 255), -1, cv2.LINE_AA)
    dilate = cv2.dilate(frame.copy(), kernel, iterations=2) 
    erode = cv2.erode(frame.copy(), kernel, iterations=2) 
    cv2.imshow("Gambar orisinil", frame)
    cv2.imshow("Gambar dilasi", dilate)
    cv2.imshow("Gambar erosi", erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def dilasi():
    kernel = np.ones((10, 10), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=2) 
    cv2.imshow("Sebelum dilasi", img_dilate)
    cv2.imshow("Sesudah dilasi", dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def erosi():
    kernel = np.ones((2, 2), np.uint8)
    erode = cv2.erode(gray_erode, kernel, iterations=1) 
    cv2.imshow("Sebelum erosi", img_erode)
    cv2.imshow("Sesudah erosi", erode)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def nDilasi():
    cv2.namedWindow(title_window_dilate)
    cv2.createTrackbar('kernel', title_window_dilate, 3, 10, fungsi_trackbar_ukuran_kernel_dilasi)
    cv2.createTrackbar('iteration', title_window_dilate, 1, 10, fungsi_trackbar_iterasi_dilasi)
    fungsi_trackbar_ukuran_kernel_dilasi(3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar_ukuran_kernel_dilasi(val):
    if val > 0:
        global kernel_size
        kernel_size = val
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        dilating = cv2.dilate(thresh, kernel, iterations=iterate)
        cv2.imshow(title_window_dilate, dilating)
    

def fungsi_trackbar_iterasi_dilasi(val):
    if val > 0:
        global iterate 
        iterate = val
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        dilating = cv2.dilate(thresh, kernel, iterations=iterate)
        cv2.imshow(title_window_dilate, dilating)


def ngErosi():
    cv2.namedWindow(title_window_erode)
    cv2.createTrackbar('kernel', title_window_erode, 3, 10, fungsi_trackbar_ukuran_kernel_erosi)
    cv2.createTrackbar('iteration', title_window_erode, 1, 10, fungsi_trackbar_iterasi_erosi)
    fungsi_trackbar_ukuran_kernel_erosi(3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar_ukuran_kernel_erosi(val):
    if val > 0:
        global kernel_size
        kernel_size = val
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        eroding = cv2.erode(gray_erode, kernel, iterations=iterate) 
        cv2.imshow(title_window_erode, eroding)
    

def fungsi_trackbar_iterasi_erosi(val):
    if val > 0:
        global iterate 
        iterate = val
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        eroding = cv2.erode(gray_erode, kernel, iterations=iterate) 
        cv2.imshow(title_window_erode, eroding)


if __name__ == "__main__":
    while True:
        inputan = input("silahkan dipilih :\n1. pengenalan\n2. mengaplikasikan erosi\n3. mengaplikasikan dilasi\n4. erosi dengan trackbar\n5. dilasi dengan trackbar\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            pengenalan()

        elif inputan == '2':
            erosi()

        elif inputan == '3':
            dilasi()

        elif inputan == '4':
            ngErosi()

        elif inputan == '5':
            nDilasi()

        else:
            break