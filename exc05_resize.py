import cv2
import numpy as np

"""
resizeCompare() -> untuk memodifikasi ukuran (pixel) sebuah gambar, tambah kecil / besar
INTER NEAREST digunakan ketika xxx
INTER LINEAR digunakan ketika ingin mengscale up gambar
INTER AREA digunakan ketika ingin meng shrink image
INTER CUBIC digunakan ketika ingin mengscale up gambar, walau lambat, tp hasilnya berkkualitas HD

"""

title_window = "Gambar orisinil"
is_resize = False
img = cv2.imread("gambar/sharingan.jpg")
h, w, c = img.shape
yt, xt, last_yt, last_xt = h, w, h, w
background = np.zeros((int(h*1.7), int(w*1.7), c)).astype(np.uint8)
bg_h, bg_w, bg_c = background.shape


def resizeGambar(event, x, y, flags, param):
    global xt, yt, bg_w, bg_h, is_resize

    if event == cv2.EVENT_LBUTTONDOWN:
        xt, yt = x, y
        is_resize = True

    elif event == cv2.EVENT_MOUSEMOVE:
        xt, yt = x, y 

        if xt > bg_w:
            xt = bg_w
        if yt > bg_h:
            yt = bg_h

    elif event == cv2.EVENT_LBUTTONUP:
        is_resize = False


def komparasiResize():
    image = cv2.imread("gambar/glookosa_banner1.jpg")
    height, weight, channel = image.shape
    rasio = 0.4  
    heightX = int(height * rasio)
    weightX = int(weight * rasio)

    img_x_resize = cv2.resize(image, (weightX, heightX))
    img_x_resize_fxy = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)  
    img_x_resize_InterNearest = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    img_x_resize_InterCubic = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    img_x_resize_InterArea = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('Gambar awal', image)
    cv2.imshow('Rasio 40%', img_x_resize)
    cv2.imshow('Rasio 1/2', img_x_resize_fxy)
    cv2.imshow('Inter nearest', img_x_resize_InterNearest)
    cv2.imshow('Inter cubic', img_x_resize_InterCubic)
    cv2.imshow('Inter area', img_x_resize_InterArea)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. membandingkan fungsi resize\n2. resize dengan klik\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            komparasiResize()

        elif inputan == '2':
            cv2.namedWindow(title_window)
            cv2.setMouseCallback(title_window, resizeGambar)
            while True:
                template = background.copy()
                if is_resize:
                    template[:yt, :xt] = cv2.resize(img, (xt, yt))
                    last_yt, last_xt = yt, xt
                else:
                    template[:last_yt, :last_xt] = cv2.resize(img, (last_xt, last_yt))
                cv2.imshow(title_window, template)
                if cv2.waitKey(1) == ord('q'):
                    break   
            cv2.destroyAllWindows()

        else:
            break