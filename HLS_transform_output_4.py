import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
from statistics import mean
from sklearn import preprocessing

def second_HLS(file_path):
    # file direction
    img = cv2.imread(file_path)
    a = []
    b = []

    # start and end point
    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            a.append(x)
            b.append(y)
            cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
            cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        1.0, (0, 0, 0), thickness=1)
            cv2.imshow("image", img)
            # print(x, y)


    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)
    cv2.waitKey(0)

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
    # x = np.mat(list(range(1, 1+abs(a[1]-a[0])))).T
    # x = np.array(list(range(1, 1+abs(a[1]-a[0]))))
    x = list(range(0, 1+abs(a[1]-a[0])))

    for i in value:
        r1 = i[0]
        r.append(r1)
        g1 = i[1]
        g.append(g1)
        b1 = i[2]
        b.append(b1)

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

    # normalization (i-min)/(max-min) and update feature list
    # set_max_h, set_min_h = max(h), min(h)
    # h = np.array([(i - set_min_h) / (set_max_h - set_min_h) for i in h])
    # set_max_l, set_min_l = max(l), min(l)
    # l = np.array([(i - set_min_l) / (set_max_l - set_min_l) for i in l])
    # set_max_s, set_min_s = max(s), min(s)
    # s = np.array([(i - set_min_s) / (set_max_s - set_min_s) for i in s])

    # second method of normalization
    # set_mean_h, set_variance_h = mean(h), np.var(h)
    # h = np.array([(i - set_mean_h) / set_variance_h for i in h])
    # set_mean_l, set_variance_l = mean(l), np.var(l)
    # l = np.array([(i - set_mean_l) / set_variance_l for i in l])
    # set_mean_s, set_variance_s = mean(s), np.var(s)
    # s = np.array([(i - set_mean_s) / set_variance_s for i in s])

    # the third way to normalize
    h = preprocessing.normalize([h])
    h = [x for x in h[0]]
    l = preprocessing.normalize([l])
    l = [x for x in l[0]]
    s = preprocessing.normalize([s])
    s = [x for x in s[0]]

    normal_hls = np.mat(np.vstack((h,l,s)))

    p4 = plt.plot(x,h, label='H')
    p5 = plt.plot(x,l, label='L')
    p6 = plt.plot(x,s, label='S')
    plt.legend()
    plt.grid()
    plt.show()


    # second chromatic transform
    mid = (len(x) - 1) / 2

    # r_second
    rs_s = 0
    rs_h = 0
    rs_l = 0
    # three filters
    k_rs = -1 / mid
    # y_rs = k_rs * x + 1
    for r_second in range(0, math.ceil(mid)):
        y_rs = k_rs * r_second + 1
        rs_s_temp = s[r_second] * y_rs
        rs_s = rs_s + rs_s_temp

        rs_h_temp = h[r_second] * y_rs
        rs_h = rs_h + rs_h_temp

        rs_l_temp = l[r_second] * y_rs
        rs_l = rs_l + rs_l_temp

    # g_second
    gs_s = 0
    gs_h = 0
    gs_l = 0

    k_gs = 1 / (len(x) - 1 - mid)
    # y_gs = k_gs * (x - mid)
    for g_second in range(math.ceil(mid), len(x)):
        y_gs = k_gs * (g_second - mid)
        gs_s_temp = s[g_second] * y_gs
        gs_s = gs_s + gs_s_temp

        gs_h_temp = h[g_second] * y_gs
        gs_h = gs_h + gs_h_temp

        gs_l_temp = l[g_second] * y_gs
        gs_l = gs_l + gs_l_temp

    # b_second
    bs_s1, bs_h1, bs_l1 = 0, 0, 0
    bs_s2, bs_h2, bs_l2 = 0, 0, 0

    k_bs1 = 1 / mid
    # y_bs1 = k_bs1 * x
    for b_second in range(0, math.ceil(mid)):
        y_bs1 = k_bs1 * b_second
        bs_s_temp = s[b_second] * y_bs1
        bs_s1 = bs_s1 + bs_s_temp

        bs_h_temp = h[b_second] * y_bs1
        bs_h1 = bs_h1 + bs_h_temp

        bs_l_temp = l[b_second] * y_bs1
        bs_l1 = bs_l1 + bs_l_temp

    k_bs2 = -1 / (len(x) - 1 - mid)
    # y_bs2 = k_bs2 * (x - mid) + 1
    for b_second in range(math.ceil(mid), len(x)):
        y_bs2 = k_bs2 * (b_second - mid) + 1
        bs_s_temp2 = s[b_second] * y_bs2
        bs_s2 = bs_s2 + bs_s_temp2

        bs_h_temp2 = h[b_second] * y_bs2
        bs_h2 = bs_h2 + bs_h_temp2

        bs_l_temp2 = l[b_second] * y_bs2
        bs_l2 = bs_l2 + bs_l_temp2

    bs_s = bs_s1 + bs_s2
    bs_h = bs_h1 + bs_h2
    bs_l = bs_l1 + bs_l2

    # print(rs_h)
    # filter_second = np.mat([[rs_h,rs_l,rs_s],
    #                  [bs_h,bs_l,bs_s],
    #                  [gs_h,gs_l,gs_s]])

    h_h,l_h,s_h = hls_transfer(rs_h,gs_h,bs_h)
    h_l,l_l,s_l = hls_transfer(rs_l,gs_l,bs_l)
    h_s,l_s,s_s = hls_transfer(rs_s,gs_s,bs_s)

    # print(h_h,l_h,s_h)
    # show complete data
    np.set_printoptions(suppress=True)
    final = np.mat([[h_h,l_h,s_h],
                    [h_s,l_s,s_s]])
    return final
