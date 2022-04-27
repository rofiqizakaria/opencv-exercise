import cv2
import numpy as np

if __name__ == '__main__':
    images = ['gambar/plat/plat1.jpg','gambar/plat/plat2.jpg','gambar/plat/plat3.jpg','gambar/plat/plat4.jpg','gambar/plat/plat5.jpg']
    img_img = []
    for i in images:
        img_img.append(cv2.imread(i))

    img1 = cv2.imread("gambar/gloo_whatsapp.jpg")
    img2 = cv2.imread("gambar/gloo_title.jpg")
    img3 = cv2.imread("gambar/gloo_describe.jpg")
    img = img_img[1]

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    frame = img.copy()
    h_img, w_img, c_img = img.shape

    for i, j in enumerate(contours):
        area = cv2.contourArea(j)
        perimeter = cv2.arcLength(j, True)
        cv2.drawContours(img, j, -1, (250, 190, 40), 3) # mereplikasi / menduplikasi contour tiap tiap objek 
        print (f'luas: {area}\t & keliling: {int(perimeter)} \tmasing2 objek')

        epsilon = 0.1 * perimeter
        approx = cv2.approxPolyDP(j, epsilon, True)
        cv2.polylines(img, [approx], True, (100,255,0), 1) # poliline full / kisut tiap tiap objek

        rect = cv2.boundingRect(j)
        x, y, w, h = rect

        aspek_rasio = w/h
        tinggi_rasio = h/h_img
        x_aspek_rasio = aspek_rasio > 0.1 and aspek_rasio < 0.9
        x_tinggi_rasio = tinggi_rasio > 0.1 and tinggi_rasio < 0.9

        if x_aspek_rasio and x_tinggi_rasio:
            roi = frame[y:y+h, x:x+w] # mendapatkan cropping tiap tiap objek
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,100,255), 2) # menandai tiap tiap objek dengan bounding box
            cv2.imshow(f'contour croppping {i}', roi) # menampilkan hasil cropping tiap tiap objek

    cv2.imshow('Contour - Method External', img)
    cv2.imshow('Contour - Menandai dengan Persegi', frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()