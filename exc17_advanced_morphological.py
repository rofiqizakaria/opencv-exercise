from time import daylight
import cv2
import numpy as np

"""
cv2.morphologyEx(img, morphological_type, kernel_iteration) 
morphological_type :
opening cv2.MORPH_OPEN (erosi lalu dilanjutkan dilasi) biasanya digunakan untuk menghapus noisy 
closing cv2.MORPH_CLOSE (dilasi lalu dilanjutkan erosi) biasanya digunakan untuk menghapus lubang kecil
gradient cv2.MORPH_GRADIENT biasanya untuk menampilkan outline dari sebuah objek

    -> fungsi_kernel_baru():
penggunaan kernel = cv2.getStructuringElement(shape, ksize, anchor) bisa lebih baik ketimbang pakai np.ones
shape = cv2.MORPH_RECT (rectangular), cv2.MORPH_CROSS (cross-shape), cv2.MORPH_ELLIPSE (eclipse)
ksize = tuple of kernel 

"""


def morphBuka():
    img = cv2.imread('gambar/mriscan.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((2, 2), np.uint8)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel, iterations=1)

    cv2.imshow('Gambar orisinil',img)
    cv2.imshow('Opening',opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def morphTutup():
    img = cv2.imread('gambar/dotted_char.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((10, 10), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

    cv2.imshow('Gambar orisinil',img)
    cv2.imshow('Closing',closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def morphBukaTutup():
    img = cv2.imread('gambar/slicedot_char.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=7)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=13)

    cv2.imshow('Gambar orisinil',img)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def morphGradasi():
    img = cv2.imread('gambar/char.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=1) 
    erode = cv2.erode(thresh, kernel, iterations=1)

    gradient1 = dilate - erode
    gradient2x = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1) 
    gradient2t = cv2.morphologyEx(gradient1, cv2.MORPH_GRADIENT, kernel, iterations=1) 

    image = cv2.imread('gambar/struk.png')
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gradience = cv2.morphologyEx(grey, cv2.MORPH_GRADIENT, kernel, iterations=1) 

    image2 = cv2.bitwise_not(cv2.imread('gambar/sidikjari.jpg'))
    grey2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    xret2, xthresh2 = cv2.threshold(grey2, 127, 255, cv2.THRESH_TOZERO_INV)
    gradience2 = cv2.morphologyEx(grey2, cv2.MORPH_GRADIENT, kernel, iterations=1) 

    cv2.imshow('Gambar orisinil',img)
    cv2.imshow('Gradient 1',gradient1)
    cv2.imshow('Gradient 2 dari img',gradient2x)
    cv2.imshow('Gradient 2 dari gradient1',gradient2t)
    cv2.imshow('Gradience ',gradience)
    cv2.imshow('Gradience 2 ',gradience2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_kernel_baru():
    img = cv2.imread('gambar/sliced_char.png')
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    dilate = cv2.dilate(thresh, kernel, iterations=7)  
    cv2.imshow("Sebelum", img)
    cv2.imshow("Sesudah", dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    


if __name__ == "__main__":    
    while True:
        inputan = input("silahkan dipilih :\n1. buka morph\n2. tutup morph\n3. buka tutup morph\n4. gradasi morph\n5. fungsi_kernel_baru\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            morphBuka()

        elif inputan == '2':
            morphTutup()

        elif inputan == '3':
            morphBukaTutup()

        elif inputan == '4':
            morphGradasi()

        elif inputan == '5':
            fungsi_kernel_baru()

        else:
            break