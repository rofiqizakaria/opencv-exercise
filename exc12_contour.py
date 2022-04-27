import cv2
import numpy as np

"""     -> contour():
cv2.findContours(img, mode, method)
mode = approx none & approx simple, kalau approx none itu marking semua tepi, kalau approx simple hanya ujung2nya saja
method RETR_EXTERNAL hanya mencontour sisi luarnya saja
method RETR_TREE mencontour samapi ke dalam dalamnya
cv2.drawContours(img, contour, contour_index, (b,g,r), thickness)
jika contour_index bernilai negatif, maka semua contour akan ter drawn

"""

img = cv2.imread("gambar/contour.jpg")
imgx = cv2.imread("gambar/hcontour.jpeg")
img_ktp = cv2.imread("gambar/ktp_agung.jpg")
img_ktpx = cv2.imread("../../../Dokumen/Data Diri/ktp_png.png")


def contour():
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    frame = img.copy()

    for i, j in enumerate(contours):
        area = cv2.contourArea(j)
        perimeter = cv2.arcLength(j, True)
        cv2.drawContours(img, j, -1, (250, 190, 40), 1)                                     # mereplikasi / menduplikasi contour tiap tiap objek 
        print (f'luas: {area}\t & keliling: {int(perimeter)} \tmasing2 objek')

        epsilon = 0.1 * perimeter
        approx = cv2.approxPolyDP(j, epsilon, True)
        cv2.polylines(img, [approx], True, (100,255,0), 1)                                  # poliline full / kisut tiap tiap objek

        rect = cv2.boundingRect(j)
        x, y, w, h = rect
        roi = frame[y:y+h, x:x+w]                                                           # mendapatkan cropping tiap tiap objek
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,100,255), 2)                            # menandai tiap tiap objek dengan bounding box
        cv2.imshow(f'contour croppping {i}', roi)                                           # menampilkan hasil cropping tiap tiap objek

    cv2.imshow('Contour - metode external', img)
    cv2.imshow('Contour - menandai dengan persegi', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def latihan_pake_ktp():
    h_img, w_img, c_img = img_ktp.shape
    ktp_gray = cv2.cvtColor(img_ktp, cv2.COLOR_BGR2GRAY)

    # thresh, binary = cv2.threshold(ktp_gray, 127, 255, cv2.THRESH_BINARY)
    thresh, binary = cv2.threshold(ktp_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
    # thresh, binary = cv2.threshold(ktp_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) # fungsi ini berlaku jika gambar aslinya tidak memungkinkan secara invert biner, karena tidak terdapat tepi tepi secara kontras

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        # cv2.drawContours(img_ktp, i, -1, (255,0,255), 0)
        rect = cv2.boundingRect(i)
        x, y, w, h = rect
        aspek_rasio = w/h
        tinggi_rasio = h/h_img
        x_aspek_rasio = aspek_rasio > 0.7 and aspek_rasio < 0.9
        x_tinggi_rasio = tinggi_rasio > 0.4 and tinggi_rasio < 0.5

        if x_aspek_rasio and x_tinggi_rasio:
            roi = img_ktp[y:y+h, x:x+w]
            cv2.rectangle(img_ktp, (x,y), (x+w, y+h), (255,0,255), 2)
            cv2.imshow('Foto tercrop', roi)
            cv2.imshow('Biner', binary)
            cv2.imshow('Foto terdeteksi', img_ktp)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. contour\n2. latihan dengan KTP\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            contour()

        elif inputan == '2':
            latihan_pake_ktp()

        else:
            break