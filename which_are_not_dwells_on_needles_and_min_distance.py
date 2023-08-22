from Dwell_Position import Dwell
from pydicom import dcmread
import numpy as np
from sklearn.cluster import KMeans
import plotly.graph_objects as go
import pandas as pd



dwell_=Dwell("/home/sebquet/Desktop/Richard_2022/1194868_Anon")

dwells=dwell_.get_dwell_list()

for i in range(len(dwells)):
    dwells[i][0]=int((dwells[i][0]+275)/0.9179688) #275 is -(x of image position of patient). 0.9179688 is from x of Pixel spacing. same for other two rows (but for y and z).
    dwells[i][1]=int((dwells[i][1]+407.5)/0.9179688)
    dwells[i][2]=int((dwells[i][2]-22.969482)/3)


files=['/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT44.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT55.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT45.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT12.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT11.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT32.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT42.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT29.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT22.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon//CT15.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT50.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT49.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT54.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT34.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT1.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT23.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT25.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT39.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT41.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT35.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT36.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT13.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT30.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT7.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT4.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT14.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT5.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT46.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT52.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT9.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT47.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT56.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT53.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT40.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT17.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT18.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT51.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT20.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT27.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT2.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT16.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT6.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT26.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT21.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT8.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT38.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT10.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT48.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT28.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT37.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT31.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT24.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT19.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT33.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT43.dcm', '/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT3.dcm']


a=[]

for i in range(len(files)):
   
   a.append(dcmread(files[i]).pixel_array)


w = np.array(a, dtype=float)
w=w.swapaxes(0,2)

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

flattened=w.flatten()

nb_class = 6

rescaled= flattened.reshape(-1,1)
kmeans = KMeans(n_clusters=nb_class, init='k-means++') #based on the commented graph below, n_clusters could be 3 to 5, but 6 gives best results for us


kmeans.fit(rescaled)

predict= kmeans.predict(rescaled)

# SSE = []
# for cluster in range(1,20):
#     kmeans = KMeans(n_clusters = cluster, init='k-means++')
#     kmeans.fit(rescaled)
#     SSE.append(kmeans.inertia_)


# frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})
# plt.figure(figsize=(12,6))
# plt.plot(frame['Cluster'], frame['SSE'], marker='o')
# plt.xlabel('Number of clusters')
# plt.ylabel('Inertia')
# plt.show()




dict_classes = {}

for i in range(nb_class):
    dict_classes["class{}".format(i)] = []


for i in range(len(predict)):
    dict_classes["class{}".format(predict[i])].append(i)


nb_in_each_class={}

for i in range(nb_class):
    nb_in_each_class["class{}".format(i)] = 0

    

def xyz(u): #transforms "flattened" position to x, y,z position
    e=list(w.shape)
    z=u//(e[0]*e[1])
    y=(u-z*(e[0]*e[1]))//(e[0])
    x=(u-z*(e[0]*e[1])-y*e[0])
    return [x, y, z]

xyz_positions={}
for i in range(nb_class):
    xyz_positions["class{}".format(i)] = []

for i in range (len(dict_classes)):
    for y in range(len(dict_classes["class{}".format(i)])):
        xyz_positions["class{}".format(i)].append(xyz(dict_classes["class{}".format(i)][y]))


def distance(n, m): #finds the distance between two [x,y,z] type of points
    o=((n[0]-m[0])**2+(n[1]-m[1])**2+(n[2]-m[2])**2)**(1/2)
    return o

distances={}
for i in range(nb_class):
    distances["class{}".format(i)] = {}

for i in range(len(distances)):
    for y in range(len(xyz_positions["class{}".format(i)])):
        distances["class{}".format(i)]["voxel{}".format(y)]=[]
        



for i in range(len(xyz_positions)):
    for y in range(len(xyz_positions["class{}".format(i)])):
        xyz_positions["class{}".format(i)][y][0]+=int(min(x1)-3)
        xyz_positions["class{}".format(i)][y][1]+=int(min(y1)-3)
        xyz_positions["class{}".format(i)][y][2]+=int(min(z1)-3)

for i in range (len(xyz_positions)):
    for y in range(len(xyz_positions["class{}".format(i)])):
        for h in range(len(dwells)):
            distances["class{}".format(i)]["voxel{}".format(y)].append(distance(xyz_positions["class{}".format(i)][y], dwells[h]))

for i in range(len(xyz_positions)):
    for y in range(len(xyz_positions["class{}".format(i)])):
        for h in range(len(dwells)):
            if xyz_positions["class{}".format(i)][y]==dwells[h]:
                nb_in_each_class["class{}".format(i)]+=1


distance_to_closest_dwell={}
for i in range(nb_class):
    distance_to_closest_dwell["class{}".format(i)] = {}

for i in range(nb_class):
    for y in range(len(distances["class{}".format(i)])):
        distance_to_closest_dwell["class{}".format(i)]["voxel{}".format(y)]={}

for i in range(nb_class):
    for y in range(len(distances["class{}".format(i)])):
        distance_to_closest_dwell["class{}".format(i)]["voxel{}".format(y)]=min(distances["class{}".format(i)]["voxel{}".format(y)])


print("----------------------------------------------------------------------------------")
print("The number of dwell positions per class:",nb_in_each_class)
print("----------------------------------------------------------------------------------")

most_=max(nb_in_each_class, key=nb_in_each_class.get)
print("The class with the highest number of dwell positions is",most_)
print("----------------------------------------------------------------------------------")





average_distance_to_closest_dwell= {}
for i in range(nb_class):
    average_distance_to_closest_dwell["class{}".format(i)]=[]

for i in range(nb_class):
        average_distance_to_closest_dwell["class{}".format(i)].append(sum(distance_to_closest_dwell["class{}".format(i)].values())/len(distance_to_closest_dwell["class{}".format(i)]))
    
print("Average distance to closest dwell in each class:",average_distance_to_closest_dwell)
print("----------------------------------------------------------------------------------")
how_many_voxels_that_are_not_dwells={}
for i in range(nb_class):
    how_many_voxels_that_are_not_dwells["class{}".format(i)] = {}

for i in range(len(how_many_voxels_that_are_not_dwells)):
    how_many_voxels_that_are_not_dwells["class{}".format(i)]=len(dict_classes["class{}".format(i)])-nb_in_each_class["class{}".format(i)]

ratio_of_voxels_that_are_dwells={}
for i in range(nb_class):
    ratio_of_voxels_that_are_dwells["class{}".format(i)] = {}

for i in range(len(ratio_of_voxels_that_are_dwells)):
    ratio_of_voxels_that_are_dwells["class{}".format(i)]=str((nb_in_each_class["class{}".format(i)]/len(dict_classes["class{}".format(i)]))*100)+"%"


print("The ratio of voxels that are dwell positions in each class",ratio_of_voxels_that_are_dwells)
print("----------------------------------------------------------------------------------")
print("The number of voxels in each class that are not dwells",how_many_voxels_that_are_not_dwells)

# #showing needles?
# X, Y, Z = np.mgrid[157:249:92j, 174:232:58j, 11:36:25j]

# l=[]
# for i in range(len(w.shape)):
#     l.append(w.shape[i]+1)
# array= np.full(shape=l, fill_value=0)

# for i in range(len(xyz_positions)):
#     for y in range(len(xyz_positions["class{}".format(i)])):
#         xyz_positions["class{}".format(i)][y][0]-=int(min(x1)-3)
#         xyz_positions["class{}".format(i)][y][1]-=int(min(y1)-3)
#         xyz_positions["class{}".format(i)][y][2]-=int(min(z1)-3)

# for i in range(len(dict_classes)):
#     if i == int(most_.replace("class","")):
#         for y in range(len(xyz_positions["class{}".format(i)])):
#             array[xyz_positions["class{}".format(i)][y][0]][xyz_positions["class{}".format(i)][y][1]][xyz_positions["class{}".format(i)][y][2]]=1

# flattened2= array.flatten()

# fig = go.Figure(data=go.Volume(
#     x=X.flatten(),
#     y=Y.flatten(),
#     z=Z.flatten(),
#     value= flattened2,
#     isomin=np.ndarray.min(flattened2),
#     isomax=np.ndarray.max(flattened2),
#     cmin=np.ndarray.min(flattened2),
#     cmax=np.ndarray.max(flattened2),
#     opacity=0.1,  
#     surface_count=30,
    
#     ))
# fig.show()
