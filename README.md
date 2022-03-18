# chromatic-transformation
This is the Y2 project of ELEC222 of the university of Liverpool. The project title is image processing on cuttlefish with light compensation.

The file ChromaticTrans.py shows the basic procedure of the whole project. "Sham_1068625-0.png" is used as an example fish and the relationship of H(H) and H(L) is used as an example combination of second HLS values. After choosing two points, the program can detect the RGB values of each pixel between these two points and tranfer the RGB values into the first HLS values. The second HLS values are then calculated automatically for analysis.
When you want to use your own picture, file path should be changed at two places, which are line 31 and line 56.

The HLS_transform_output_4.py is similar to ChromaticTrans.py. However, it omits lightness (L) as a variable in the output since lightness is more unstable during the project. We focused on the hue (H) and saturation (S) instead. The file is defined as a method for other files to use to improve the coding cohesion.

The file method.py defines three methods. "assgin" determines the file path and implements the chromatic transform. "average" calculates the average values of second HLS values based on different time of the same fish (t = 0 or 5 or 10). "fun" implements the random plots of 15 different combinations of second HLS values.

The file plotallaverage.py uses the method.py on all types of cuttlefish. Features of different fish can be plotted as a point in one figure for analysis.

The file LightCompensation.py implements the light compensation to achieve the same L of different time of the same fish. Two points should be chosen on the background of the fish images to calcualte the average lightness of the images. The difference can be calculated between time. After applying the conclusion from light compensation (G value should increase 4.5% and B value should increase 12% if the lightness difference of two figures is 10), G and R values can be changed to achieve the same L.

The file ColorModulation.py uses LightCompensation.py on sham1068625 as an example.
