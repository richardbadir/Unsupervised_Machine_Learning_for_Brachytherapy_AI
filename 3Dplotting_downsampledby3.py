from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from pydicom import dcmread
import plotly.graph_objects as go


files=['/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT44_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT55_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT45_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT12_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT11_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT32_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT42_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT29_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT22_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT15_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT50_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT49_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT54_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT34_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT1_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT23_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT25_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT39_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT41_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT35_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT36_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT13_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT30_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT7_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT4_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT14_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT5_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT46_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT52_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT9_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT47_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT56_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT53_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT40_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT17_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT18_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT51_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT20_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT27_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT2_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT16_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT6_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT26_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT21_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT8_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT38_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT10_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT48_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT28_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT37_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT31_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT24_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT19_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT33_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT43_downsampled.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT3_downsampled.dcm']


a=[]

for i in range(len(files)):
   
   a.append(dcmread(files[i]).pixel_array)

w= np.array(a)


X, Y, Z = np.mgrid[0:56:56j, 0:171:171j, 0:171:171j]

fig = go.Figure(data=go.Volume(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value= w.flatten(),
    isomin=np.ndarray.min(w),
    isomax=np.ndarray.max(w),
    cmin=np.ndarray.min(w),
    cmax=np.ndarray.max(w),
    opacity=0.1,  
    surface_count=30,
    ))
fig.show()