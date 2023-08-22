import numpy as np
from pydicom import dcmread
import plotly.graph_objects as go
import glob



files= ["/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT44.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT55.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT12.dcm"]

h=[]

for i in range(len(files)):
   
   h.append(dcmread(files[i]).pixel_array)



w= np.array(h)
n=np.swapaxes(w,0,1)

X, Y, Z = np.mgrid[0:3:3j, 0:512:512j, 0:512:512j]

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


