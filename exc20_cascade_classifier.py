import cv2
import numpy as np

"""
Class cv2.CascadeClassifier() digunakan untuk membaca classifier file (.xml)
Pada class cv2.CascadeClassifier() terdapat method .detectMultiscale() untuk melakukan deteksi objek pada sebuah citra.
Method .detectMultiscale() memiliki beberapa parameter input,
    scaleFactor : Ukuran seberapa besar input image direduksi agar mampu dibaca oleh detector algorithm. Hal inilah yang memungkinkan algorima dapat mendeteksi wajah dalam beragam skala gambar (multi scale image).
    minNeighbors : Ukuran minimum antara posisi face rectangle satu terhadap lainya. Hal ini berkaitan dengan method .detectMultiscale() yang akan melakukan sliding window terhadap image. Jika kita set ke 0, maka banyak false positive face rectangle terdeteksi. sehingga kita akan pilih nilai yang lebih tinggi. Namun jangan sampai memilih nilai yang terlalu besar, yang mengakibatkan true positive face rectangle menjadi tidak terdeteksi.
    flags : Parameter yang sama pada method cvHaarDetectObjects. Ini tidak digunakan pada Cascade Classifier terbaru.
    minSize : Ukuran object minimal. Ukuran yang lebih kecil tidak akan dimasukan kedalam detected object.
    maxSize : Ukuran object maksimal. Ukuran yang lebih besar tidak akan dimasukan kedalam detected object.

"""

face_cc = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml') 
eye_cc = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml') 
plat_cc = cv2.CascadeClassifier('haarcascade/license_plate_cascade.xml') 
mobil_cc = cv2.CascadeClassifier('haarcascade/haarcascade_cars.xml') 
img_lena = cv2.imread('gambar/sweety.jpg')
img_mata1 = cv2.imread('gambar/mata/mata2.jpg')
img_plat = cv2.imread('gambar/plat/plat-nomor-5.jpg')


def deteksi(title ,image, object_cascade):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    objects = object_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in objects:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(130,40,250),2)

    cv2.imshow(f'gambar {title}',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def deteksi_kendaraan(title ,image, plat_cascade):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if title == 'plat':
        object = plat_cascade.detectMultiScale(gray, scaleFactor=1.06, minNeighbors=3, minSize=(90, 30))
    elif title == 'mobil':
        object = plat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x,y,w,h) in object:
        image = cv2.rectangle(image,(x,y),(x+w,y+h),(130,40,250),2)

        img_roi = image[y:y+h, x:x+w]
        cv2.imshow('plate',img_roi)

    cv2.imshow(f'gambar {title}',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def deteksi_wajah_mata(image, face_cascade, eye_cascade):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

    for (x,y,w,h) in faces:
        xImg = cv2.rectangle(image, (x, y), (x+w, y+h), (40,250,130)) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = xImg[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (x, y, w, h) in eyes:
            cv2.rectangle(roi_color, (x, y), (x+w, y+h), (130,40,250)) 

    cv2.imshow(f'gambar wajah & mata',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def mobil_detected():
    car_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_cars.xml')
    cap = cv2.VideoCapture("video/mobil_di_tol.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('Detect Cars', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cv2.destroyAllWindows()


def mobil_counting_detected():
    car_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_cars.xml')
    cap = cv2.VideoCapture("video/mobil_di_tol.mp4")
    count = 0
    prev_y = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
        h, w, c = frame.shape
        x1, y1, x2, y2 = int(w*0.1), int(h*0.8), int(w*0.9), int(h*0.8)        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, minNeighbors=5)

        for (x, y, w, h) in cars:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cy = (y+h//2)

            if (y1 - 30) < cy and (y1 + 30) > cy and abs(prev_y - cy) > 20:
                count +=1
                prev_y = cy

        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
        cv2.putText(frame, "Vehicle Count : %d" % count, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 1, cv2.LINE_AA)  
        cv2.imshow('Detect Cars', frame)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    # deteksi('mata lena', img_lena, eye_cc)
    # deteksi('wajah lena', img_lena, face_cc)
    # deteksi('mata someone', img_mata1, eye_cc)
    # deteksi_kendaraan('plat', img_plat, plat_cc)

    # deteksi_wajah_mata(img_lena, face_cc, eye_cc)
    # mobil_detected()
    mobil_counting_detected()

