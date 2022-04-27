import os
import cv2

if __name__ == '__main__':
    img = cv2.imread("gambar/sharingan.jpg")
    h, w, c = img.shape
    image_organ = cv2.imread("../gambar/organ.png")
    size_sharingan_compressed = os.path.getsize("gambar/sharingan.jpg")/1024                # jpeg compressed file (in kb)
    print(f'type data image sharingan berupa: {type(img)}')
    print(f"tinggi gambar: {h}")
    print(f"lebar gambar: {w}")
    print(f"channel gambar: {c}")
    print(f"jumlah pixel gambar: {h*w}")
    print(f"ukuran kompresi file: {size_sharingan_compressed} kb")
    print(f"berapa banyak item matrix yg terbuat: {img.size}")

    # <<<<< Access Image Channel >>>>>
    blue_pixel = img[:, :, 0]                                                               # untuk access pixel layer Blue
    green_pixel = img[:, :, 1]                                                              # untuk access pixel layer Green
    red_pixel = img[:, :, 2]                                                                # untuk access pixel layer Red
    print('\nAccess Image Channel')
    print(f'pixel Blue: \n{blue_pixel.shape}')
    print(f'pixel Green: \n{green_pixel.shape}')
    print(f'pixel Red: \n{red_pixel.shape}')

    # <<<<< Access Individual Pixel >>>>>
    px_blue_130x250, px_green_130x250, px_red_130x250 = img[130, 250]                       # mengecheck nilai lokasi pixel 130x250
    print('\nAccess Individual Pixel')
    print(f"nilau pixel di lokasi 130x250 \nR: {px_blue_130x250}, G: {px_green_130x250}, B: {px_red_130x250}")