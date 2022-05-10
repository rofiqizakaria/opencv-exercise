import cv2 
import numpy as np 

if __name__ == '__main__':
    wajah_casecade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml') 
    mata_casecade = cv2.CascadeClassifier('haarcascade/haarcascade_eye.xml') 
    # tangkap = cv2.VideoCapture('rtsp://192.168.207.240:8080/video/h264')                     # bisa juga link url sebuah kamera lain
    tangkap = cv2.VideoCapture(0)                     
    tangkap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    tangkap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    # cv2.VideoWriter
    # while(tangkap.isOpened()):
    #     ret, frame = tangkap.read()
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     banyak_mata = mata_casecade.detectMultiScale(gray, 1.1, 4)

    #     for (x,y,w,h) in banyak_mata:
    #         frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(130,40,250),2)

    #     if ret:
    #         cv2.imshow('Frame', frame)

    #         if cv2.waitKey(1) == ord('q'):                                                  # jika tekan 'q' maka berhenti
    #             break                                                                       

    #     else:                                                                               # jika sumber penamngkapan gambar/video (kamera) mati, maka otomatis akan berhenti juga
    #         break
        
    # tangkap.release()
    # cv2.destroyAllWindows()


    cv2.VideoWriter
    while(tangkap.isOpened()):
        ret, frame = tangkap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        banyak_wajah = wajah_casecade.detectMultiScale(gray, 1.3, 5) 
        banyak_mata = mata_casecade.detectMultiScale(gray, 1.1, 4)

        for (x,y,w,h) in banyak_wajah:
            frameX = cv2.rectangle(frame, (x, y), (x+w, y+h), (40,250,130)) 
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frameX[y:y+h, x:x+w]
            banyak_mata = mata_casecade.detectMultiScale(roi_gray)

            for (x, y, w, h) in banyak_mata:
                cv2.rectangle(roi_color, (x, y), (x+w, y+h), (130,40,250)) 
                
        if ret:
            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) == ord('q'):                                                  # jika tekan 'q' maka berhenti
                break                                                                       

        else:                                                                               # jika sumber penamngkapan gambar/video (kamera) mati, maka otomatis akan berhenti juga
            break
        
    tangkap.release()
    cv2.destroyAllWindows()



