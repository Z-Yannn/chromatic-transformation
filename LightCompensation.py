import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
from statistics import mean
from sklearn import preprocessing
import scipy.misc as smp

def second_HLS_noselection(file_path,input_x, input_y):
    # file direction
    img = cv2.imread(file_path)
    a = []
    b = []
    a = input_x
    b = input_y

    coordin = np.mat([[a[0],b[0]],
                      [a[1],b[1]]])
    print(coordin)
    # slope of the line
    k = (b[1] - b[0]) / (a[1] - a[0])

    imgg = Image.open(file_path)
    redImage = imgg.convert('RGB')

    # rgb value
    value = []
    for x in range(min(a[0], a[1]), max(a[0], a[1])+1):
        # line
        y = k * (x - a[1]) + b[1]
        pix = list(redImage.getpixel((x,y)))
        value.append(pix)

    # print(value)

    # original rgb
    r = []
    g = []
    b = []

    # draw the three lines
    x = list(range(0, 1+abs(a[1]-a[0])))

    for i in value:
        r1 = i[0]
        r.append(r1)
        g1 = i[1]
        g.append(g1)
        b1 = i[2]
        b.append(b1)

    # def smallpix(arr):
    #     leng = math.floor(len(arr) / 9)
    #     fin = []
    #
    #     u = 0
    #     while u < 9:
    #         sum = 0
    #         for i in range(u * leng, (u + 1) * leng):
    #             temp = arr[i]
    #             sum += temp
    #         avg = sum / leng
    #         fin.append(avg)
    #         u += 1
    #     return fin
    #
    # r = smallpix(r)
    # g = smallpix(g)
    # b = smallpix(b)
    # print(r,g,b)
    # each pixel rgb value
    p1 = plt.plot(x,r,'r-', label='r')
    p2 = plt.plot(x,g,'g-', label='g')
    p3 = plt.plot(x,b,'b-', label='b')
    plt.legend()
    plt.grid()
    plt.show()


    def hls_transfer(red, green, blue):
        rr = red - min(red, green, blue)
        gg = green - min(red, green, blue)
        bb = blue - min(red, green, blue)

        if rr == 0:
            h = 240 - 120 * gg / (gg + bb)
        if gg == 0:
            h = 360 - 120 * bb / (bb + rr)
        if bb == 0:
            h = 120 - 120 * rr / (rr + gg)

        l = (red + green + blue) / 3

        high = (max(red, green, blue) - min(red, green, blue))
        low = (max(red, green, blue) + min(red, green, blue))
        s = high / low

        return h, l, s

    # first chromatic transform
    h = []
    l = []
    s = []
    for m in value:
        rx = m[0]
        gx = m[1]
        bx = m[2]
        hh, ll, ss = hls_transfer(rx, gx, bx)

        h.append(hh)
        l.append(ll)
        s.append(ss)

    p4 = plt.plot(x,h, label='H')
    p5 = plt.plot(x,l, label='L')
    p6 = plt.plot(x,s, label='S')
    plt.legend()
    plt.grid()
    plt.show()

    # sum
    Lenh = len(h)
    Lens = len(s)
    lenl = len(l)
    sumh = 0
    sums = 0
    suml = 0
    for i in h:
        sumh = sumh + i
    avgh = sumh / Lenh
    for j in s:
        sums = sums + j
    avgs = sums / Lens
    for m in l:
        suml = suml + m
    avgl = suml / lenl

    return avgl

def changeRGB1(file_path):
    omb = 0.12
    omg = 0.045

    imgg = Image.open(file_path)
    mage = imgg.convert('RGB')
    array = np.array(mage)
    cols,rows = mage.size

    red = []
    green = []
    blue = []
    for i in range(cols):
        for j in range(rows):
            pix = mage.getpixel((i,j))
            bb = pix[2] + pix[2] * omb * (14/10)

            blue.append(bb)
            gg = pix[1] + pix[1] * omg * (14/10)
            green.append(gg)
            red.append(pix[0])
    fina = []
    for o in range(len(red)):
        fin = red[o],green[o],blue[o]
        tempp = list(fin)
        fina.append(tempp)

    f = 0
    while f < len(fina):
        for p in range(cols):
            for q in range(rows):
                array[q,p] = fina[f]
                f += 1
    new_img = Image.fromarray(array)
    new_img.show()
    # new_img.save("/Users/DELL/Desktop/result/sham_1068625_0_after.png")

def changeRGB2(file_path):
    omb = 0.12
    omg = 0.045

    imgg = Image.open(file_path)
    mage = imgg.convert('RGB')
    array = np.array(mage)
    cols, rows = mage.size

    red = []
    green = []
    blue = []
    for i in range(cols):
        for j in range(rows):
            pix = mage.getpixel((i,j))
            bb = pix[2] - pix[2] * omb

            blue.append(bb)
            gg = pix[1] - pix[1] * omg
            green.append(gg)
            red.append(pix[0])
    fina = []
    for o in range(len(red)):
        fin = red[o],green[o],blue[o]
        tempp = list(fin)
        fina.append(tempp)

    f = 0
    while f < len(fina):
        for p in range(cols):
            for q in range(rows):
                array[q,p] = fina[f]
                f += 1
    new_img = Image.fromarray(array)
    new_img.show()
    # new_img.save("/Users/DELL/Desktop/result/sham_1068625_10_after.png")



