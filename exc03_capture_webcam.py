import os
import cv2

if __name__ == '__main__':

    tangkap = cv2.VideoCapture(0)
    tangkap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    tangkap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    keluaran = cv2.VideoWriter('hasil_rekaman_webcam.mp4', fourcc, 20, (320, 240))

    cv2.VideoWriter
    while(tangkap.isOpened()):
        ret, frame = tangkap.read()
        if ret:
            keluaran.write(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
    tangkap.release()
    keluaran.release()
    cv2.destroyAllWindows()