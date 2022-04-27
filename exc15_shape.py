import cv2
from matplotlib.pyplot import draw
import numpy as np
import math

"""
cv2.HoughLines(img, rho, theta, threshold, lines, srn, stn)
cv2.HoughLinesP(img, rho, theta, threshold, lines, minLinLength, maxLineGap) # for probabilistic
rho = the resolution of the parameter r in pixels, we use 1 pixel
theta = the resolution of the parameter 0 in radians, we use 1 degree (np.pi/180)
threshold = the minimum of intersection to detect a line
lines = a vector that will store the parameter (r, U) of the detected lines
minLinLength = the minimum numbers of points that can form a lin. Lines with less than this numberes of points are disregarded
maxLineGap = the maximum gap between two points to be considered in the same time
cv2.HoughCircles(img, mode, dp, min_dist_center, param1, param2, min_radius, max_radius)
mode = cv2.HOUGH_STANDARD, cv2.HOUGH_PROBABILISTIC, cv2.HOUGH_MULTI_SCALE, cv2.HOUGH_GRADIENT
dp = the inverse ratio of resolution (default 1)
min_dist_center = minimum distance between detected centers
param1 = upper threshold for the internal canny edge detector
param2 = threshold for center detection
min_radius = radius minimal to be detected, default 0
max_radius = radius maximal to be detected, default 0

"""

img1 = cv2.imread('gambar/road.jpeg')
img2 = cv2.imread('gambar/road2.jpeg')
img3 = cv2.imread('gambar/mata/mata5.jpg')
img = img3
h, w, c = img.shape
max_value = 300
default_value = 150
min_radius = 21
max_radius = 30
param1 = 200
param2 = 17
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0, 0)
edges = cv2.Canny(gray, 50, 200)
title_window_line = 'Transformasi hough garis'
title_window_circle = 'Transformasi hough lingkaran'
min_line_length = 100
max_line_gap = 20


def garisHough():
    cv2.namedWindow(title_window_line)
    cv2.createTrackbar('thresh', title_window_line,default_value, max_value, fungsi_trackbar)
    fungsi_trackbar(default_value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def fungsi_trackbar(val):
    frame = img.copy()
    lines = cv2.HoughLines(edges, 1, np.pi / 100, val, None, 0, 0)

    if lines is not None:
        for i in lines:
            rho = i[0][0]
            theta = i[0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1, y1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            x2, y2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(frame, (x1, y1), (x2, y2), (255, 130, 70), 1, cv2.LINE_AA)

    cv2.imshow(title_window_line, frame)


def probabilitasGarisHough():
    cv2.namedWindow(title_window_line)
    cv2.createTrackbar('Celah maximal', title_window_line, 20, 200, fungsi_trackbar_maximal_celah_garis)
    cv2.createTrackbar('Panjang minimal', title_window_line, 100, 200, fungsi_trackbar_minimal_panjang_garis)
    fungsi_trackbar_minimal_panjang_garis(100)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
def ngedraw_garis(lines):
    frame = img.copy()
    if lines is not None:
        for i in lines:
            x1, y1, x2, y2 = i[0]
            cv2.line(frame, (x1, x2), (x2, y2), (255, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow(title_window_line, frame)


def fungsi_trackbar_minimal_panjang_garis(val):
    global min_line_length
    min_line_length = val
    lines = cv2.HoughLinesP(edges, 1, np.pi/100, 50, minLineLength=min_line_length, maxLineGap=max_line_gap)
    ngedraw_garis(lines)


def fungsi_trackbar_maximal_celah_garis(val):
    global max_line_gap
    max_line_gap = val
    lines = cv2.HoughLinesP(edges, 1, np.pi/100, 50, minLineLength=min_line_length, maxLineGap=max_line_gap)
    ngedraw_garis(lines)


def lingkaranHough():
    cv2.namedWindow(title_window_circle)
    cv2.createTrackbar('Radius minimal', title_window_circle, 21, 50, fungsi_trackbar_radius_minimal)
    cv2.createTrackbar('Radius maximal', title_window_circle, 30, 50, fungsi_trackbar_radius_maximal)
    cv2.createTrackbar('Parameter 1', title_window_circle, 200, 255, fungsi_trackbar_parameter1)
    cv2.createTrackbar('Parameter 2', title_window_circle, 17, 30, fungsi_trackbar_parameter2)
    fungsi_trackbar_radius_minimal(min_radius)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def ngedraw_lingkaran(circles):
    frame = img.copy()
    if circles is not None:
        circles = np.uint8(np.around(circles))[0]
        for i in circles:
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow(title_window_circle, frame)


def fungsi_trackbar_radius_minimal(val):
    global min_radius
    min_radius = val
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, h/64, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    ngedraw_lingkaran(circles)


def fungsi_trackbar_radius_maximal(val):
    global max_radius
    max_radius = val
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, h/64, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    ngedraw_lingkaran(circles)


def fungsi_trackbar_parameter1(val):
    global param1
    param1 = val
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, h/64, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    ngedraw_lingkaran(circles)


def fungsi_trackbar_parameter2(val):
    global param2
    param2 = val
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, h/64, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
    ngedraw_lingkaran(circles)


if __name__ == "__main__":
    while True:
        inputan = input("silahkan dipilih :\n1. garis hough\n2. menghitung kemungkinan garis hough\n3. lingkaran hough\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            garisHough()

        elif inputan == '2':
            probabilitasGarisHough()

        elif inputan == '3':
            lingkaranHough()

        else:
            break