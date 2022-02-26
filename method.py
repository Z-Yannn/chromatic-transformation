import matplotlib.pyplot as plt
import numpy as np
import HLS_transform_output_4 as hls
import HLS_transform_no_selection as hls2
import os

def assign(path):
    final = []
    a = os.listdir(path)

    for x in a:
        str1 = path + '/' + x
        final_temp = hls.second_HLS(str1)
        final.append(final_temp)

    return final


def average(m):
    d = np.zeros((m[0].shape[0], m[0].shape[1]))

    for i in range(m[0].shape[0]):
        for j in range(m[0].shape[1]):
            d[i, j] = (m[0][i, j] + m[1][i, j] + m[2][i, j]) / 3

    return d


def fun(matt, colors):
    g1 = []

    for k in matt:
        m = []
        for i in range(k.shape[0]):
            for j in range(k.shape[1]):
                m.append(k[i,j])
        g1.append(m)

    x_st = []
    y_st = []
    x_st_final = []
    for i in g1:
        leng = len(i)
        x_st_temp = []
        y_st_temp = []
        for xx in range(leng):
            for yy in range(leng):
                if yy > xx:
                    x_st_temp.append(i[xx])
                    y_st_temp.append(i[yy])

        x_st.append(x_st_temp)
        y_st.append(y_st_temp)
    print(x_st)

    for u in range(15):
        plotx = []
        ploty = []
        for v in range(len(x_st)):
            # print(v,u)
            plotx.append(x_st[v][u])
            ploty.append(y_st[v][u])
        x = np.array(plotx)
        y = np.array(ploty)
        plt.scatter(x, y, c=colors)
        plt.grid()
        if u == 0:
            plt.xlabel('H(H)')
            plt.ylabel('L(H)')
        if u == 1:
            plt.xlabel('H(H)')
            plt.ylabel('S(H)')
        if u == 2:
            plt.xlabel('H(H)')
            plt.ylabel('H(S)')
        if u == 3:
            plt.xlabel('H(H)')
            plt.ylabel('L(S)')
        if u == 4:
            plt.xlabel('H(H)')
            plt.ylabel('S(S)')
        if u == 5:
            plt.xlabel('L(H)')
            plt.ylabel('S(H)')
        if u == 6:
            plt.xlabel('L(H)')
            plt.ylabel('H(S)')
        if u == 7:
            plt.xlabel('L(H)')
            plt.ylabel('L(S)')
        if u == 8:
            plt.xlabel('L(H)')
            plt.ylabel('S(S)')
        if u == 9:
            plt.xlabel('S(H)')
            plt.ylabel('H(S)')
        if u == 10:
            plt.xlabel('S(H)')
            plt.ylabel('L(S)')
        if u == 11:
            plt.xlabel('S(H)')
            plt.ylabel('S(S)')
        if u == 12:
            plt.xlabel('H(S)')
            plt.ylabel('L(S)')
        if u == 13:
            plt.xlabel('H(S)')
            plt.ylabel('S(S)')
        if u == 14:
            plt.xlabel('L(S)')
            plt.ylabel('S(S)')
        plt.show()
