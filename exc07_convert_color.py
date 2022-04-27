import cv2

"""
grayscale = interpretasi abu abu
rgb = red, gree, blue
hsv = hue, saturation, value 
hls = hue, lightness, saturation 
lab = lightness, a-color, b-color
cmyk = cyan, magenta, yellow, key
    
    hue itu code indikator tiap tiap warna itu sendiri
    saturation itu representasi kepucatan pada sebuah warna, dari mulai puyeh hingga warna asli
    value itu representasi kecerahan (brightness) pada buah warna, dari mulai hitam sampai warna asli
    lightness sama seperti value, yg membedakan adalah dimulai dari hitam sampai putih, ditengah2 adalah nilai optimum sebuah warna asli
    a-color itu merah atau hijau sedangkan b-color itu biru atau kuning
    key itu hitam

pencarian nilai abu-abu adalah dgn berikut 0.299 R + 0.587 G + 0.114 B

"""

if __name__ == '__main__':
    img = cv2.imread("gambar/sharingan.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    cv2.imshow('Gambar Asli', img)
    cv2.imshow('Gambar Grayscale', img_gray)
    cv2.imshow('Gambar RGB', img_rgb)
    cv2.imshow('Gambar BGRA', img_bgra)
    cv2.imshow('Gambar HSV', img_hsv)
    cv2.imshow('Gambar HLS', img_hls)
    cv2.imshow('Gambar LAB', img_lab)
    cv2.waitKey(0)
    cv2.destroyAllWindows()