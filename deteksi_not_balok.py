from xml.dom import HierarchyRequestErr
import cv2 

def studicase_notbalok():
    img = cv2.imread('gambar/not_balok.png')
    xgray = cv2.bitwise_not(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    ret, thresh = cv2.threshold(xgray, 100, 255, cv2.THRESH_BINARY)

    # mendeteksi garis untuk kebutuhan manipulasi
    h, w, c = img.shape
    horizontal_size = w // 30
    vertical_size = h // 30
    horizontal_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    vertical_structure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
    horizontal_opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_structure, iterations=1)
    vertical_opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, vertical_structure, iterations=1)

    contours, hierarchy = cv2.findContours(vertical_opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i in contours:
        cv2.drawContours(img, [i], -1, (0,0,255), 1)

    cv2.imshow("contours", img)
    cv2.imshow("mempertahankan garis", horizontal_opening)
    cv2.imshow("menghapus garis", vertical_opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    


if __name__ == "__main__":
    studicase_notbalok()