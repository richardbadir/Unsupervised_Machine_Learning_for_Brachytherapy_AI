from Dwell_Position import Dwell
from pydicom import dcmread
import numpy as np
import plotly.graph_objects as go


dwell_=Dwell("/home/sebquet/Desktop/Richard_2022/1194868_Anon")

dwells=dwell_.get_dwell_list()

for i in range(len(dwells)):
    dwells[i][0]=int((dwells[i][0]+275)/0.9179688)
    dwells[i][1]=int((dwells[i][1]+407.5)/0.9179688)
    dwells[i][2]=int((dwells[i][2]-22.969482)/3)


files=['/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT44.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT55.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT45.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT12.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT11.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT32.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT42.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT29.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT22.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon//CT15.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT50.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT49.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT54.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT34.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT1.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT23.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT25.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT39.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT41.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT35.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT36.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT13.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT30.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT7.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT4.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT14.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT5.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT46.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT52.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT9.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT47.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT56.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT53.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT40.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT17.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT18.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT51.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT20.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT27.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT2.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT16.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT6.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT26.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT21.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT8.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT38.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT10.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT48.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT28.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT37.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT31.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT24.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT19.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT33.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT43.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT3.dcm']


a=[]

for i in range(len(files)):
   
   a.append(dcmread(files[i]).pixel_array)


w = np.array(a, dtype=float)
w=w.swapaxes(0,2)
for i in range(len(w)):
    for j in range(len(dwells)):
        if i == dwells[j][0]:
            for k in range(len(w[i])):
                if k == dwells[j][1]:
                    for h in range(len(w[i][k])):
                        if h == dwells[j][2]:
                            w[i][k][h]= 40000
                            

x1=[]
y1=[]
z1=[]
for n in range (len(dwells)):
    x1.append(dwells[n][0])
for n in range (len(dwells)):
    y1.append(dwells[n][1])
for n in range (len(dwells)):
    z1.append(dwells[n][2])


w=w[int(min(x1)-3):int(max(x1)+4),int(min(y1)-3):int(max(y1)+4),int(min(z1)-3):int(max(z1)+4)]

X, Y, Z = np.mgrid[157:249:92j, 174:232:58j, 11:36:25j]

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
print(w.shape)