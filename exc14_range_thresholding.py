from msilib.schema import MsiAssembly
import cv2
from cv2 import imshow
import numpy as np

img_glookosa = cv2.imread("gambar/glookosa_logo_awal.jpg")
img_blueberry = cv2.imread("gambar/blueberry.jpg")
img_strawberry = cv2.imread("gambar/strawberry.jpg")
h, w, c = img_glookosa.shape


def pengenalan():
    # <<<<< kenapa pake kurung 3 karena 3D >>>>>
    red = np.uint8([[[0, 0, 255]]])
    green = np.uint8([[[0, 255, 0]]])
    blue = np.uint8([[[255, 0, 0]]])
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    print (f'Warna merah RGB dalam HSV : {hsv_red}')
    print (f'Warna hijau RGB dalam HSV : {hsv_green}')
    print (f'Warna biru RGB dalam HSV : {hsv_blue}')


def seleksiRGBkeHSV():
    hsv = cv2.cvtColor(img_glookosa, cv2.COLOR_BGR2HSV)

    # <<<<< menginisialisasi jarak dari warna merah di HSV >>>>>
    lower_red = np.array([-18, 25, 25])
    upper_red = np.array([10, 255, 255])
    # <<<<< menginisialisasi jarak dari warna hijau di HSV >>>>>
    lower_green = np.array([40, 25, 25])
    upper_green = np.array([80, 255, 255])
    # <<<<< menginisialisasi jarak dari warna biru di HSV >>>>>
    lower_blue = np.array([100, 25, 25])
    upper_blue = np.array([130, 255, 255])

    # <<<<< menginisialisasi jarak dari warna oranye di HSV >>>>>
    lower_orange = np.array([15, 25, 25])
    upper_orange = np.array([23, 255, 255])
    # <<<<< menginisialisasi jarak dari warna kuning di HSV >>>>>
    lower_yellow = np.array([23, 25, 25])
    upper_yellow = np.array([30, 255, 255])
    # <<<<< menginisialisasi jarak dari warna ungu di HSV >>>>>
    lower_purple = np.array([130, 25, 25])
    upper_purple = np.array([170, 255, 255])

    # <<<<< threshold gambar HSV untuk mendapatkan hanya warna tertentu >>>>>
    mask_red = cv2.inRange(hsv.copy(), lower_red, upper_red) 
    mask_green = cv2.inRange(hsv.copy(), lower_green, upper_green) 
    mask_blue = cv2.inRange(hsv.copy(), lower_blue, upper_blue) 
    mask_orange = cv2.inRange(hsv.copy(), lower_orange, upper_orange) 
    mask_yellow = cv2.inRange(hsv.copy(), lower_yellow, upper_yellow) 
    mask_purple = cv2.inRange(hsv.copy(), lower_purple, upper_purple) 

    res_red = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_red)
    res_green = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_green)
    res_blue = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_blue)
    res_orange = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_orange)
    res_yellow = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_yellow)
    res_purple = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_purple)

    mask_total = mask_red + mask_green + mask_blue + mask_orange + mask_yellow + mask_purple
    res_total = cv2.bitwise_and(img_glookosa, img_glookosa, mask=mask_total)

    frame = np.zeros((h*2, w*3, c )).astype(np.uint8)                                       # inisiasi banyak gambar dalam 1 frame
    frame[0:h, 0:w] = res_red
    frame[0:h, w:2*w] = res_green
    frame[0:h, 2*w:3*w] = res_blue
    frame[h:2*h, 0:w] = res_orange
    frame[h:2*h, w:2*w] = res_yellow
    frame[h:2*h, 2*w:3*w] = res_purple
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  

    cv2.imshow('Cek berdasarkan warna masing2 rgb', frame)
    cv2.imshow("Gambar orisinil", img_glookosa)
    cv2.imshow("Gambar total modif", res_total)
    cv2.imshow("Gambar total mask ", mask_total)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    while True:
        inputan = input("silahkan dipilih :\n1. pengenalan\n2. menyeleksi RGB ke HSV\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            pengenalan()

        elif inputan == '2':
            seleksiRGBkeHSV()

        else:
            break