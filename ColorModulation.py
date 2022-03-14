import LightCompensation as hls2

l0 = hls2.second_HLS_noselection('/Users/DELL/Desktop/result/data/Origin/sham1068625/Sham_1068625-0.png',[3,40],[40,3])
l5 = hls2.second_HLS_noselection('/Users/DELL/Desktop/result/data/Origin/sham1068625/Sham_1068625-5.png',[3,40],[40,3])
l10 = hls2.second_HLS_noselection('/Users/DELL/Desktop/result/data/Origin/sham1068625/Sham_1068625-10.png',[3,40],[40,3])

delta1 = l5 - l0
delta2 = l10 - l5
print(delta1,delta2)

hls2.changeRGB1('/Users/DELL/Desktop/result/data/Origin/sham1068625/Sham_1068625-0.png')

hls2.changeRGB2('/Users/DELL/Desktop/result/data/Origin/sham1068625/Sham_1068625-10.png')

# 2
# l0 = hls.second_HLS('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-0.png')
# l5 = hls.second_HLS('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-5.png')
# l10 = hls.second_HLS('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-10.png')

# l0 = hls2.second_HLS_noselection('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-0.png',[10,30],[40,15])
# l5 = hls2.second_HLS_noselection('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-5.png',[10,30],[40,15])
# l10 = hls2.second_HLS_noselection('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-10.png',[10,30],[40,15])
# delta1 = l5 - l0
# delta2 = l10 - l5
# print(delta1,delta2)
#
# hls2.changeRGB1('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-0.png')
#
# hls2.changeRGB2('/Users/DELL/Desktop/result/data/sham1069495/Sham_1069495-10.png')
