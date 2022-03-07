# chromatic-transformation
This is the Y2 project of ELEC222 of the university of Liverpool. The project title is image processing on cuttle fish with light compensation.

The file FirstChromaticTrans.py shows the progress of the first week. After choosing two points, the program can detect the RGB values of each pixel between these two points and automatically tranfer the RGB values into the first HLS values.
When you want to use your own picture, file path should be changed at two places.

The HLS_transform_output_4.py implements the first and second chromatic transform in sequence. After implementing the first transform, the first HLS values are normalized. Then three second rgb filters are applied and transfered the first HLS values into 9 new RGB. These new RGB values are implemented by the basic chromatic transform again. Then 9 second HLS values are available. However, the output omits when the variables are L. For example, R(L), G(L) and B(L).

The file method.py defines three method. "assgin" implements the file path. "average" implements the average value of second HLS values based on different time of the same fish (t = 0 or 5 or 10). "fun" implements the random plots of 15 different combinations of second HLS values.

The file "LightCompensation" implements the light compensation to achieve the same L of different time of the same fish. The light difference should be calculated first manaually.
