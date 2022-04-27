import cv2
import numpy as np

"""
cv2.canny(img, threshMin, threshMax)
Digunakan untuk mencari batas2 objek pada gambar dengan mengamati pixel2 yg berubah drastis => non maximum supression

"""

title_window_edgedetection = 'ini image edge detection'
edge_max = 255
edge_default = 127
current_min = 0
current_max = 255
img = cv2.imread("gambar/sharingan.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def fungsi_trackbar_batas_minimal(val):
    global current_min
    current_min = val
    edge = cv2.Canny(gray, current_min, current_max)
    cv2.imshow(title_window_edgedetection, edge)


def fungsi_trackbar_batas_maxmimal(val):
    global current_max
    current_max = val
    edge = cv2.Canny(gray, current_min, current_max)
    cv2.imshow(title_window_edgedetection, edge)


if __name__ == "__main__":
    cv2.namedWindow(title_window_edgedetection)
    cv2.createTrackbar('min', title_window_edgedetection,edge_default, edge_max, fungsi_trackbar_batas_minimal)
    cv2.createTrackbar('max', title_window_edgedetection,edge_default, edge_max, fungsi_trackbar_batas_maxmimal)
    fungsi_trackbar_batas_minimal(0)
    cv2.imshow('Gambar orisinil', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()