import numpy as np
import plotly.graph_objects as go

a=[[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,5,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]]
x= np.array(a)
print(x.shape)


def xyz(u): #transforms "flattened" position to x, y,z position
    e=list(x.shape)
    # for i in range(len(e)):
        # e[i]+=1
    z=u//(e[0]*e[1])
    y=(u-z*(e[0]*e[1]))//(e[0])
    x1=(u-z*(e[0]*e[1])-y*e[0])
    return [x1, y, z]
u=x.flatten

o=0
for i in range(len(a)):
    for i2 in range(len(a[i])):
        for i3 in range(len(a[i][i2])):
           o+=1
for i in range(o):
    print("{}:".format(i)+"{}".format(xyz(i)))

def xyz1(u): #transforms "flattened" position to x, y,z position
    e=list(x.shape)
    for i in range(len(e)):
        e[i]+=1
    z=u//(e[0]*e[1])
    y=(u-z*(e[0]*e[1]))//(e[0])
    x1=(u-z*(e[0]*e[1])-y*e[0])
    return [x1, y, z]
print("------------------------------")

l=0
for i in range(len(a)):
    for i2 in range(len(a[i])):
        for i3 in range(len(a[i][i2])):
           l+=1
for i in range(o):
    print("{}:".format(i)+"{}".format(xyz1(i)))
print("-----------------------")



