import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


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


img = cv2.imread('/Users/DELL/Desktop/result/data/sham1068625/Sham_1068625-0.png')
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

# slope of the line
k = (b[1] - b[0]) / (a[1] - a[0])

imgg = Image.open('/Users/DELL/Desktop/result/data/sham1068625/Sham_1068625-0.png')
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

# each pixel rgb value
p1 = plt.plot(x,r,'r-', label='r')
p2 = plt.plot(x,g,'g-', label='g')
p3 = plt.plot(x,b,'b-', label='b')
plt.legend()
plt.grid()
plt.show()


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
