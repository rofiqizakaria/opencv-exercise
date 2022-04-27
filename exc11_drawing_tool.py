from tkinter import Y
import cv2 
import numpy as np
import math

"""
cv2.line(img, (x0,y0), (xt,yt), (B,G,R), thickness, line_type)
(x0,y0) = titik awal, (xt,yt) = titik akhir, (B, G, R) = warna garis, thickness = ketebalan, line_type = type2 garis
cv2.rectangle(img, (x0,y0), (xt,yt), (B,G,R), thickness, line_type)
(x0,y0) = pojok kiri atas, (xt,yt) = pojok kanan bawah, (B, G, R) = warna garis, thickness = ketebalan, line_type = type2 garis
cv2.circle(img, (x,y), radius, (B,G,R), thickness, line_type)
(x,y) = titik pusat, radius = jari-jari, (B, G, R) = warna garis, thickness = ketebalan, line_type = type2 garis
cv2.putText(img, text, (x,y), font_type, font_scale, (B,G,R), thickness, line_type)
(x,y) = titik kiri atas, text, string yg akan kita tulis, font_type = tipe font yg ada di opencv, font_scale = ukursan string, (B, G, R) = warna garis, thickness = ketebalan textnya, line_type = type2 garis

"""

background = np.zeros((400,400,3)).astype(np.uint8)
background2 = np.zeros((200,600,3)).astype(np.uint8)
h2, w2, c2 = background2.shape
x0, y0, xt, yt, r = 0,0,0,0,0
title_window_line = "ngGambar Garis"
title_window_circle = "ngGambar Lingkaran"
title_window_rectangle = "ngGambar Persegi"
is_draw = False
frame = np.ones((400,400,3)).astype(np.uint8)*255


def gambarGaris():
    cv2.line(background, (100,350), (300,350), (50,0,255), 3, cv2.FILLED)                   # membuat garis horizontal 
    cv2.line(background, (50,100), (50,300), (25,255,0), 9, cv2.LINE_8)                     # membuat garis vertical 

    cv2.namedWindow(title_window_line)
    cv2.setMouseCallback(title_window_line, ngeread_garis)
    ngedraw_garis(x0, y0, xt, yt)
    cv2.imshow('Gambar garis', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ngedraw_garis(x0, y0, xt, yt):
    background = frame.copy()
    cv2.line(background, (x0,y0), (xt,yt), (70,40,200), 5, cv2.LINE_AA)
    cv2.imshow(title_window_line, background)


def ngeread_garis(event, x, y, flags, param):
    global x0, y0, xt, yt, is_draw

    if event == cv2.EVENT_LBUTTONDOWN:
        x0, y0, xt, yt = x, y, x, y
        is_draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        xt, yt = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        xt, yt = x, y
        is_draw = False

    if is_draw:
        ngedraw_garis(x0, y0, xt, yt)


def gambarPersegi():
    cv2.rectangle(background, (19,25), (200, 150), (130,0,255), -1)                         # membuat persegi dengan fill color
    cv2.rectangle(background, (210,50), (270, 270), (100,200,255), 7, cv2.LINE_AA)          # membuat persegi dengan outline color

    cv2.namedWindow(title_window_rectangle)
    cv2.setMouseCallback(title_window_rectangle, ngeread_persegi)
    ngedraw_persegi(x0, y0, xt, yt)
    cv2.imshow('Gambar persegi', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ngedraw_persegi(x0, y0, xt, yt):
    background = frame.copy()
    cv2.rectangle(background, (x0,y0), (xt,yt), (100,250,130), 5, cv2.LINE_AA)
    cv2.imshow(title_window_rectangle, background)


def ngeread_persegi(event, x, y, flags, param):
    global x0, y0, xt, yt, is_draw

    if event == cv2.EVENT_LBUTTONDOWN:
        x0, y0, xt, yt = x, y, x, y
        is_draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        xt, yt = x, y
    
    elif event == cv2.EVENT_LBUTTONUP:
        xt, yt = x, y
        is_draw = False

    if is_draw:
        ngedraw_persegi(x0, y0, xt, yt)


def gambarLingkaran():
    cv2.circle(background, (65,250), 55, (0, 55, 250), -1, cv2.LINE_AA)                     # membuat lingkaran dengan fill color, jika set negatif, maka ter fill semuanya
    cv2.circle(background, (65,65), 55, (0, 255, 150), 2, cv2.LINE_AA)                      # membuat lingkaran dengan outline color,  jika set positif, ex:7, maka hanya outline saja

    cv2.namedWindow(title_window_circle)
    cv2.setMouseCallback(title_window_circle, ngeread_lingkaran)
    ngedraw_lingkaran(x0, y0, r)
    cv2.imshow('Gambar lingkaran', background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ngedraw_lingkaran(x0, y0, r):
    background = frame.copy()
    cv2.circle(background, (x0,y0), r, (255,130,75), 2, cv2.LINE_AA)
    cv2.imshow(title_window_circle, background)


def ngeread_lingkaran(event, x, y, flags, param):
    global x0, y0, r, is_draw

    if event == cv2.EVENT_LBUTTONDOWN:
        x0, y0, r = x, y, 0
        is_draw = True

    elif event == cv2.EVENT_MOUSEMOVE:
        r = int(math.sqrt((x - x0)**2 + (y - y0)**2))
    
    elif event == cv2.EVENT_LBUTTONUP:
        r = int(math.sqrt((x - x0)**2 + (y - y0)**2))
        is_draw = False

    if is_draw:
        ngedraw_lingkaran(x0, y0, r)


def nulisText():
    font_types = [
        cv2.FONT_HERSHEY_COMPLEX,
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        cv2.FONT_HERSHEY_DUPLEX,
        cv2.FONT_HERSHEY_PLAIN,
        cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
        cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        cv2.FONT_HERSHEY_SIMPLEX,
        cv2.FONT_HERSHEY_TRIPLEX
    ]
    texts = [
        'FONT_HERSHEY_COMPLEX',
        'FONT_HERSHEY_COMPLEX_SMALL',
        'FONT_HERSHEY_DUPLEX',
        'FONT_HERSHEY_PLAIN',
        'FONT_HERSHEY_SCRIPT_COMPLEX',
        'FONT_HERSHEY_SCRIPT_SIMPLEX',
        'FONT_HERSHEY_SIMPLEX',
        'FONT_HERSHEY_TRIPLEX'
    ]
    for i, j in zip(texts, font_types):
        frame = background2.copy()
        cv2.putText(frame, i, (50,50), j, 0.9, (0,255,127), 1, cv2.LINE_AA)
        cv2.imshow("Tulisan", frame)
        cv2.waitKey(2000)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. menggambar garis\n2. menggambar persegi\n3. menggambar lingkaran\n4. menulis tulisan\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            gambarGaris()

        elif inputan == '2':
            gambarPersegi()

        elif inputan == '3':
            gambarLingkaran()

        elif inputan == '4':
            nulisText()

        else:
            break