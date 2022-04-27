import cv2 
import numpy as np

"""
cv2.warpAffine(img, m, (w, h)) 
m = matrik input (rotasi/translasi/scale), codenya dibawah ini:
    cv2.getRotationMatrix2D(center, degre, zoomin)
    center = titik tengah dari rotasi tuple
    degre = rotasi kemiringan
    zoomin = diperbesar / diperkecil
    cv2.getAffineTransform(pts1, pts2)
    cv2.getPerspectiveTransform(pts1x,pts2x)
        pts1 = triangle vertices source image
        pts2 = triangle vertices destination image
(w, h) = ukuran image.shape

"""

img1 = cv2.imread('gambar/blueberry.jpg')
img2 = cv2.imread('gambar/blueberry2.jpg')
img_sha = cv2.imread('gambar/sharingan.jpg')
img_gloo = cv2.imread('gambar/glookosa_logo_awal.jpg')
img_sudoku = cv2.imread('gambar/sudoku.jpg')
h, w, c = img_sha.shape
title_window_rotate = 'Rotasi gambar'
title_window_affine = 'Affine transformasi dengan klik mouse'
title_window_perspective = 'Perpective transformasi dengan klik mouse'
default_value = 45 
max_value = 360
pts1 = []
pts2 = []
pts1x = []
pts2x = np.float32([[0,0],[300,0],[300,300], [0,300]])
is_edit = False


def rotasi():
    # center = (w // 2, h // 2)
    # m = cv2.getRotationMatrix2D(center, 45, 1.3)
    # rotated = cv2.warpAffine(img_sha , m, (w, h))
    cv2.namedWindow(title_window_rotate)
    cv2.createTrackbar('angel', title_window_rotate, default_value, max_value, fungsi_trackbar_rotasi)
    fungsi_trackbar_rotasi(default_value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    


def fungsi_trackbar_rotasi(val):
    center = (w // 2, h // 2)
    m = cv2.getRotationMatrix2D(center, val, 1)
    rotated = cv2.warpAffine(img_sha , m, (w, h))
    cv2.imshow(title_window_rotate, rotated)


def affineTransformasi():
    pts1 = np.float32([[0,0],[w,0],[0,h]])
    pts2 = np.float32([[0,100],[300,50],[50,350]])
    m1 = np.float32([[1, 0, 100],[0, 1, 50]])
    m2 = cv2.getAffineTransform(pts1, pts2)
    tranlasi1 = cv2.warpAffine(img_sha, m1, (w, h))
    tranlasi2 = cv2.warpAffine(img_sha, m2, (w, h))
    cv2.imshow("Gambar orisinil", img_sha)
    cv2.imshow("Gambar tranlasi 1", tranlasi1)
    cv2.imshow("Gambar tranlasi 2", tranlasi2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    


def transformasi_affine(event, x, y, flags, param):

    global pts1, pts2, is_edit, frame

    if event == cv2.EVENT_RBUTTONDOWN:
        print ('klik kanan')
        is_edit = True
        pts1 = []
        pts2 = []
        frame = img_sha.copy()

    if event == cv2.EVENT_LBUTTONDOWN and is_edit:
        print ('klik kiri')
        if len(pts1) < 3 :
            print ('kurang lagi')
            pts1.append([x, y])
            cv2.circle(frame, (x, y), 4, (255, 255, 0), -1)

        elif len(pts2) < 3 :
            print ('kurang lagi x')
            if len(pts2) == 0:
                print ('kurang lagi xx')
                frame = np.zeros((frame.shape)).astype(np.uint8)
            pts2.append([x, y])
            cv2.circle(frame, (x, y), 4, (0, 255, 255), -1)

        else:
            w, h, c = frame.shape
            pts1 = np.float32(pts1)
            pts2 = np.float32(pts2)
            m = cv2.getAffineTransform(pts1, pts2)
            frame = cv2.warpAffine(img_sha.copy(), m, (w, h))
            is_edit = False
        

def perspectiveTransformasi():
    # <<<<< topleft, topright, bottomleft, bottomright -> tl, tr, bl, br >>>>>
    pts1 = np.float32([[56,65],[368,52],[389,390],[28,387]])    
    pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])    
    m = cv2.getPerspectiveTransform(pts1, pts2)
    output = cv2.warpPerspective(img_sudoku, m, (300,300))
    for x, y in pts1.astype(np.uint16):
        cv2.circle(img_sudoku, (x, y), 4, (255, 255, 0), -1)
    cv2.imshow('Gambar asli', img_sudoku)
    cv2.imshow('Gambar transformasi perspective', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   


def transformasi_perspective(event,x,y,flags,param):
    
    global pts1x, is_edit, frame
    
    if event == cv2.EVENT_RBUTTONDOWN:
        is_edit = True
        pts1x = []
        frame = img_sudoku.copy()
        
    if event == cv2.EVENT_LBUTTONDOWN and is_edit:
        if len(pts1x) < 4 :
            pts1x.append([x, y])
            cv2.circle(frame, (x,y), 4, (255,255,0), -1)
            
        else :
            pts1x = order_points(np.array(pts1x))
            #pts1x = np.float32(pts1x)
            m = cv2.getPerspectiveTransform(pts1x,pts2x)
            output = cv2.warpPerspective(img_sudoku, m, (300,300))
            cv2.imshow("hasil transformasi perpective", output)
            is_edit = False
                                      
                                      
def order_points(pts):
    rect = np.zeros((4,2), dtype = 'float32')
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect


if __name__ == "__main__":
    while True:
        inputan = input("silahkan dipilih :\n1. rotasi\n2. affine\n3. perspective\n4. transformasi affine (pake mouse)\n5. transformasi perspective (pake mouse)\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            rotasi()

        elif inputan == '2':
            affineTransformasi()

        elif inputan == '3':
            perspectiveTransformasi()

        elif inputan == '4':                                                                # transformasi affine
            cv2.namedWindow(title_window_affine)
            cv2.setMouseCallback(title_window_affine, transformasi_affine)
            frame = img_sha.copy()
            while True:
                cv2.imshow(title_window_affine, frame)
                if cv2.waitKey(1) == ord('q'):
                    break
            cv2.destroyAllWindows()

        elif inputan == '5':                                                                # transformasi perspective                      
            cv2.namedWindow(title_window_perspective) 
            cv2.setMouseCallback(title_window_perspective, transformasi_perspective) 
            frame = img_sudoku.copy()
            while True:
                cv2.imshow(title_window_perspective, frame)
                if cv2.waitKey(1) == ord('q') :
                    break
            cv2.destroyAllWindows()
        
        else:
            break