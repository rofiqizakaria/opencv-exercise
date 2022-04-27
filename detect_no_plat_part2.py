from xml.dom import HierarchyRequestErr
import cv2 
import os
import numpy as np 

img1 = cv2.imread('gambar/plat/plat-nomor-1.jpg')
img3 = cv2.imread('gambar/plat/plat-nomor-3.jpg')
img5 = cv2.imread('gambar/plat/plat-nomor-5.jpg')
img6 = cv2.imread('gambar/plat/plat-nomor-6.jpg')
img = img3


def casecadeAutomate():
    for filename in os.listdir("."):
        if filename.find('gambar/plat/plat-nomor-') == -1:
            continue
        img = cv2.imread(filename)

        h, w, c = img.shape
        thresh, roi = preprocessing(img, h1=0.5*h, h2=0.85*h )

        # get plate number image
        contours = get_contours(thresh)
        is_plate, plate_img = crop_plate(thresh, contours)

        if is_plate :
            # get char in detected plate number
            contours = get_contours(plate_img)
            if len(contours) > 1:
                contours, __ = sort_contours(contours)
            for i, cnt in enumerate(contours) :
                x, y, w, h = cv2.boundingRect(cnt)
                char_roi = plate_img[y:y+h, x:x+w]
                cv2.imshow("ROI Char - %d" % i, char_roi)
            cv2.imshow("plate img", plate_img)

        cv2.imshow("roi", thresh)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()


def casecade():
    h, w, c = img.shape 
    thresh, roi = preprocessing(img, h1=0.5*h, h2=0.85*h)
    
    contours = get_contours(thresh)    
    is_plate, plate_img = crop_plate(thresh, contours)

    if is_plate:
        cv2.imshow('plate img', plate_img)
        contours = get_contours(plate_img)
        if len(contours) > 1:
            contours, ret = sort_contours(contours)
            for i, cnt in enumerate(contours):
                x, y, w, h = cv2.boundingRect(cnt)
                char_roi = plate_img[y:y+h, x:x+w]
                cv2.imshow(f'ROI Char {i}', char_roi)

    cv2.imshow("roi", roi)
    cv2.imshow("thresh", thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def preprocessing(img, h1, h2): # untuk mencari region of interest
    # mendapatkan roi & resize
    h, w, c = img.shape
    roi = img[int(h1):int(h2),int(w*0.3):int(w*0.7)]
    scale = 300/roi.shape[0]
    roi = cv2.resize(roi, (0,0), fx=scale, fy=scale)

    # mengubah dari abu2 ke biner
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh, roi


def get_contours(thresh):
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    h, w, c = img.shape
    size = h*w
    contours = [cc for i, cc in enumerate(contours) if contour_char_ok(cc, size)]    
    return contours
    

def contour_char_ok(cc, size = 1000000):
    x, y, w, h, = cv2.boundingRect(cc)
    area = cv2.contourArea(cc)
    
    if w < 3 or h < 5 or area < 80:
        return False

    valid_dimension = w/h > 0.11 and w/h < 0.7
    valid_area_ratio = area/(w*h) > 0.2
    return valid_dimension and valid_area_ratio


def sort_contours(contours, method='left-to-right'):
    reverse = False
    i = 0
    if method == 'right-to-left' or method == 'bottom-to-top':
        reverse  = True
    if method == 'top-to-bottom' or method == 'bottom-to-top':
        i = 1
    bounding_boxes = [cv2.boundingRect(i) for i in contours]
    cnts, bounding_boxes = zip(*sorted(zip(contours, bounding_boxes), key=lambda b:b[1][i], reverse=reverse))
    return cnts, bounding_boxes
    
    
def crop_plate(thresh, contours):
    rects = [] 
    for i, cnt in enumerate(contours):
        rect = cv2.boundingRect(cnt)
        rects.append(rect)

    rects = np.array(rects)

    if len(rects) < 4:
        return False, thresh
    rects = similar_rect(rects, row=3, n=2)

    if len(rects) < 4:
        return False, thresh
    rects = similar_rect(rects, row=2, n=2)

    if len(rects) < 4:
        return False, thresh
    x1 = rects[:, 0].min()
    x2 = rects[:, 0].max() + rects[:, 2].max() 
    y1 = rects[:, 1].min()
    y2 = rects[:, 1].max() + rects[:, 3].max() 
    plate_number = thresh[y1:y2, x1:x2]
    return True, plate_number


def similar_rect(rects, row=3, n=2):
    mean = np.mean(rects[:, row])
    std = np.std(rects[:, row])
    rects = np.array([rect for rect in rects if abs(rect[row] - mean) < n*std and rect_ok(rect)])
    return rects


def rect_ok(rect):
    x, y, w, h = rect
    return w/h > 0.11 and w/h < 0.7


if __name__ == "__main__":
    # casecade()
    casecadeAutomate()

