import os
import cv2

if __name__ == '__main__':

    tangkap = cv2.VideoCapture(f"video/ice_cream_jeruk_murni.mp4")
    while tangkap.isOpened():
        ret, frame = tangkap.read()                                                         # memperoleh image tiap2 frame
        if ret == True:                                                                     # jika videonya masih berjalan, tetap lanjut
            cv2.imshow('Frame', frame)                                                      # menampilkan image
            if cv2.waitKey(25) == ord('q'):                                                 # kalau dipenceet 'q' maka akan close
                break

            if cv2.waitKey(25) == ord('s'):                                                 # kalau dipenceet 's' maka akan save photo persis pada frame yg terpencet
                cv2.imwrite(f"Foto dari video", frame)
        else:                                                                               # jika sudah selesai, otomatis nge close
            break
    tangkap.release()
    cv2.destroyAllWindows()