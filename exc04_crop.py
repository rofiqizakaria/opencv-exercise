import cv2

img = cv2.imread("gambar/sharingan.jpg")
h, w, c = img.shape
title_window = "Gambar orisinil"
cropped_window_name = "Crop dinamis"


def cropStatis():
    # <<<<< Crop gambar berdasarkan nilai statis >>>>>
    tinggi_40 = int(h * 0.4)                                                                # memperoleh tinggi 40% dari asli
    lebar_70 = int(w * 0.7)                                                                 # memperoleh lebar 70% dari asli
    crop_img_sha = img[0:tinggi_40, 0:lebar_70]
    cv2.imshow("Crop statis", crop_img_sha)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cropDinamis():
    # <<<<< Crop gambar berdasarkan drag n drop >>>>>
    cv2.namedWindow(title_window)
    cv2.setMouseCallback(title_window, fungsi_ngecrop)
    while True:
        cv2.imshow(title_window, img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()


def fungsi_ngecrop(event, x, y, flags, param):
    global x0, y0, xt, yt
    global tercrop

    if event == cv2.EVENT_LBUTTONDOWN:                                                      # jika tombol kiri mouse terklik
        x0, y0, xt, yt = x, y, x, y

    elif event == cv2.EVENT_MOUSEMOVE:                                                      # jika mouse bergerak
        xt, yt = x, y

    elif event == cv2.EVENT_LBUTTONUP:                                                      # jika tombol kiri mouse terlepas
        tercrop = img[y0:yt, x0:xt]

        cv2.imshow(cropped_window_name, tercrop)
        cv2.namedWindow(cropped_window_name)
        cv2.setMouseCallback(cropped_window_name, fungsi_ngesave)


def fungsi_ngesave(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:                                                      # jika klik kanan, maka akan menyimpan
        cv2.imwrite("Gambar yang telah tercrop", tercrop)


if __name__ == '__main__':
    while True:
        inputan = input("silahkan dipilih :\n1. crop statis\n2. crop dinamis\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            cropStatis()

        elif inputan == '2':
            cropDinamis()

        else:
            break