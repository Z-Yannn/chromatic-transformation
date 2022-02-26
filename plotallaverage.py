import matplotlib.pyplot as plt
import numpy as np
import HLS_transform_output_4 as hls
import HLS_transform_no_selection as hls2
import os
import method as mt

# 2AA3L1081683
finalAAL_3 = mt.assign('/Users/DELL/Desktop/result/data/Origin/2%AA3%L1081683')
AAL3 = mt.average(finalAAL_3)

# 2AA1069500
finalAA_0 = mt.assign('/Users/DELL/Desktop/result/data/Origin/2%AA1069500')
AA0 = mt.average(finalAA_0)

# 2AA1069503
finalAA_3 = mt.assign('/Users/DELL/Desktop/result/data/Origin/2%AA1069503')
AA3 = mt.average(finalAA_3)

# 2AA1080139
finalAA_9 = mt.assign('/Users/DELL/Desktop/result/data/Origin/2%AA1080139')
AA9 = mt.average(finalAA_9)

# 2AA1081178
finalAA_8 = mt.assign('/Users/DELL/Desktop/result/data/Origin/2%AA1081178')
AA8 = mt.average(finalAA_8)

# 0.5AA2L1068635
finAA5 = mt.assign('/Users/DELL/Desktop/result/data/Origin/0.5%AA2%L1068635')
halfAAL5 = mt.average(finAA5)

# 0.5AA2L1069083
finAA3 = mt.assign('/Users/DELL/Desktop/result/data/Origin/0.5%AA2%L1069083')
halfAAL3 = mt.average(finAA3)

# 0.5%AA1068337
finAA7 = mt.assign('/Users/DELL/Desktop/result/data/Origin/0.5%AA1068337')
halfAA7 = mt.average(finAA7)

# 0.5AA1068394
finAA4 = mt.assign('/Users/DELL/Desktop/result/data/Origin/0.5%AA1068394')
halfAA4 = mt.average(finAA4)


# sham1068625
finalsham_1 = mt.assign('/Users/DELL/Desktop/result/data/Origin/sham1068625')
sham1 = mt.average(finalsham_1)

# sham1069495
finalsham_2 = mt.assign('/Users/DELL/Desktop/result/data/Origin/sham1069495')
sham2 = mt.average(finalsham_2)


colors = np.array(['maroon','red','red','red','red','lime','lime','green','green','blue','blue'])
matt = [AAL3, AA0, AA3, AA9, AA8, halfAAL5, halfAAL3, halfAA7, halfAA4, sham1, sham2]

mt.fun(matt,colors)


