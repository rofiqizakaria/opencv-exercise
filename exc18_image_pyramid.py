import cv2 
import numpy as np 

"""
penggunaan pyramid ini sama halnya dengan menggunakan resize, hanya saja jika menggunakan resize prosesnya akan lebih lambat,
dikarenakan pyramid menghapus 1/2 baris x kolom pixel, sedangkan resize tidak . resize berpengaruh terhadap performance
berikut adalah penggunaanya :
    cv2.pyrDown(img, dst_size, border_type) 
    cv2.pyrDown(img, dst_size, border_type)
    dst_size adalah ukuran akhir yg akan dituju pada sebuah gambar, defaultnya yakni 1/2x ukuran awal untuk downsampling, 2x ukuran awal untuk upsampling
    border_type adalah tipe garis tepi, diantaranya:
        cv2.BORDER_DEFAULT
        cv2.BORDER_CONSTANT
        cv2.BORDER_REPLICATE
        cv2.BORDER_REFLECT
        cv2.BORDER_WRAP
        cv2.BORDER_ISOLATED

"""

img1 = cv2.imread('gambar/blueberry.jpg')
img2 = cv2.imread('gambar/blueberry2.jpg')
img_sha = cv2.imread('gambar/sharingan.jpg')
img_gloo = cv2.imread('gambar/glookosa_logo_awal.jpg')


def piramidaGaussia():
    h, w, c = img_sha.shape 
    img_pydown = cv2.pyrDown(img_sha)
    img_pyup = cv2.pyrUp(img_sha)
    img_down_up = cv2.pyrUp(img_pydown)
    img_up_down = cv2.pyrDown(img_pyup)
    cv2.imshow("Gambar orisinil", img_sha)
    cv2.imshow("pyramid down", img_pydown)
    cv2.imshow("pyramid up", img_pyup)
    cv2.imshow("pyramid down lalu up", img_down_up)
    cv2.imshow("pyramid up lalu down", img_up_down)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    


def operasiGambar():
    # addition 
    # img1 = np.ones((500,500,3)).astype(np.uint8)*50
    # img2 = np.ones((500 ,500,3)).astype(np.uint8)*127
    out_add12 = cv2.add(img1, img2)
    out_add21 = cv2.add(img2, img1)
    out_subtr12 = cv2.subtract(img1, img2)
    out_subtr21 = cv2.subtract(img2, img1)

    h_merging12 = np.hstack((out_add12, out_subtr12))
    h_merging21 = np.hstack((out_add21, out_subtr21))

    cv2.imshow("add subtract 1-2 ", h_merging12)
    cv2.imshow("add subtract 2-1 ", h_merging21)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()     


def piramidaLaplasia():
    gp_0 = img_sha
    gp_down = cv2.pyrDown(gp_0)
    gp_down_up = cv2.pyrUp(gp_down)
    lp_downup_0 = cv2.subtract(gp_down_up, gp_0)
    lp_0_downup = cv2.subtract(gp_0, gp_down_up)
    cv2.imshow("GP 0", gp_0)
    cv2.imshow("laplacian pyramid 0 downup", lp_0_downup)
    cv2.imshow("laplacian pyramid downup 0", lp_downup_0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     


def stitching():
    gp1 = img_sha.copy()
    gp1_list = [gp1]
    for i in range(6):
        gp1 = cv2.pyrDown(gp1)
        gp1_list.append(gp1)
    
    gp2 = img_gloo.copy()
    gp2_list = [gp2]
    for i in range(6):
        gp2 = cv2.pyrDown(gp2)
        gp2_list.append(gp2)

    lp1_list = [gp1_list[-1]]
    for i in range(6, 0, -1):
        lp1 = cv2.subtract(gp1_list[i-1], cv2.pyrUp(gp1_list[i]))
        lp1_list.apppend(lp1)

    lp2_list = [gp2_list[-1]]
    for i in range(6, 0, -1):
        lp2 = cv2.subtract(gp2_list[i-1],  cv2.pyrUp(gp2_list[i]))
        lp2_list.apppend(lp2)

    ls = []
    for l1, l2 in zip(lp1_list, lp2_list):
        h, w, c = l1.shape
        l = np.hstack((l1[:, :w//2], l2[:, w//2:]))
        ls.append(l)

    output = ls[0]
    for i in range(1, 7):
        output = cv2.add(cv2.pyrUp(output), ls[i])

    cv2.imshow("Stitching gambar", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()     


if __name__ == "__main__":
    while True:
        inputan = input("silahkan dipilih :\n1. piramida gaussi\n2. operasi gambar\n3. piramida laplaci\n4. stitching (masih tahap development)\ntekan 'apa aja' untuk keluar : ")

        if inputan == '1':
            piramidaGaussia()

        elif inputan == '2':
            operasiGambar()

        elif inputan == '3':
            piramidaLaplasia()

        elif inputan == '4':
            stitching() # <<<< masih dalam tahap developmment >>>>

        else:
            break