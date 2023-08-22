from Dwell_Position import Dwell
from pydicom import dcmread
import numpy as np
from sklearn.cluster import KMeans



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


nb_class=[2,3,4,5,12,17]


nbs_in_each_class={}
for i in range(len(nb_class)):
        nbs_in_each_class["{} classes".format(nb_class[i])] = {}

mosts={}
for i in range(len(nb_class)):
        mosts["{} classes".format(nb_class[i])] = {}

rescaled= flattened.reshape(-1,1)



def xyz(u): #transforms "flattened" position to x, y,z position
    e=list(w.shape)
    z=u//(e[0]*e[1])
    y=(u-z*(e[0]*e[1]))//(e[0])
    x=(u-z*(e[0]*e[1])-y*e[0])
    return [x, y, z]


for i in range(len(nb_class)):
    kmeans = KMeans(n_clusters=nb_class[i], init='k-means++') #based on the commented graph below, n_clusters could be 3 or 4
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

    for j in range(nb_class[i]):
        dict_classes["class{}".format(j)] = []


    for j in range(len(predict)):
        dict_classes["class{}".format(predict[j])].append(j)

    nb_in_each_class={}

    for j in range(nb_class[i]):
        nb_in_each_class["class{}".format(j)] = 0

    
    # for g in range(len(dwells_flattened)):
    #     for j in range(len(dict_classes)):
    #         for k in range(len(dict_classes["class{}".format(j)])):
    #             if dwells_flattened[g]==dict_classes["class{}".format(j)][k]:
    #                 nb_in_each_class["class{}".format(j)]+=1
    
    xyz_positions={}
    for k in range(nb_class[i]):
        xyz_positions["class{}".format(k)] = []

    for k in range (len(dict_classes)):
        for y in range(len(dict_classes["class{}".format(k)])):
            xyz_positions["class{}".format(k)].append(xyz(dict_classes["class{}".format(k)][y]))

    
    for k in range(len(xyz_positions)):
        for y in range(len(xyz_positions["class{}".format(k)])):
            xyz_positions["class{}".format(k)][y][0]+=int(min(x1)-3)
            xyz_positions["class{}".format(k)][y][1]+=int(min(y1)-3)
            xyz_positions["class{}".format(k)][y][2]+=int(min(z1)-3)

    for k in range(len(xyz_positions)):
        for y in range(len(xyz_positions["class{}".format(k)])):
            for h in range(len(dwells)):
                if xyz_positions["class{}".format(k)][y]==dwells[h]:
                    nb_in_each_class["class{}".format(k)]+=1


    nbs_in_each_class["{} classes".format(nb_class[i])]= nb_in_each_class
   

    most_=max(nb_in_each_class, key=nb_in_each_class.get)
    mosts["{} classes".format(nb_class[i])]= most_


print(nbs_in_each_class)
print(mosts)
