from Dwell_Position import Dwell
from pydicom import dcmread
import numpy as np
from sklearn.cluster import KMeans
import statistics

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


w=w[int(min(x1)-3):int(max(x1)+3),int(min(y1)-3):int(max(y1)+3),int(min(z1)-3):int(max(z1)+3)]

flattened=w.flatten()


centroid1=np.random.choice(flattened)
centroid2=np.random.choice(flattened)
centroid3=np.random.choice(flattened)

class1=[]
class2=[]
class3=[]
for i in range(len(flattened)):
    if abs(flattened[i]-centroid2)>abs(flattened[i]-centroid1)<abs(flattened[i]-centroid3):
        class1.append(flattened[i])
    if abs(flattened[i]-centroid1)>abs(flattened[i]-centroid2)<abs(flattened[i]-centroid3):
        class2.append(flattened[i])
    if abs(flattened[i]-centroid2)>abs(flattened[i]-centroid3)<abs(flattened[i]-centroid1):
        class3.append(flattened[i])

class11=[]
class22=[]
class33=[]
while 2!=3:
    o=0
    o+=1
    if o%2==0:
        for i in range(max(len(class1), len(class2), len(class3))):
            if i in range(len(class1)):
                if abs(class1[i]-statistics.mean(class2))>abs(class1[i]-statistics.mean(class1))<abs(class1[i]-statistics.mean(class3)):
                    class11.append(class1[i])
            if i in range(len(class2)):
                if abs(class2[i]-statistics.mean(class1))>abs(class2[i]-statistics.mean(class2))<abs(class2[i]-statistics.mean(class3)):
                    class22.append(class2[i])
            if i in range(len(class3)):
                if abs(class3[i]-statistics.mean(class2))>abs(class3[i]-statistics.mean(class3))<abs(class3[i]-statistics.mean(class1)):
                    class33.append(class3[i])
            if statistics.mean(class11)==statistics.mean(class1):
                if statistics.mean(class22)==statistics.mean(class2):
                    if statistics.mean(class33)==statistics.mean(class3):
                        break
                else:
                    for i in range(len(class1)):
                        class1.remove(class1[i])
                    for i in range(len(class2)):
                        class2.remove(class2[i])
                    for i in range(len(class3)):
                        class3.remove(class3[i])

                    else:
                        for i in range(len(class1)):
                            class1.remove(class1[i])
                        for i in range(len(class2)):
                            class2.remove(class2[i])
                        for i in range(len(class3)):
                            class3.remove(class3[i])
            else:
                for i in range(len(class1)):
                    class1.remove(class1[i])
                for i in range(len(class2)):
                    class2.remove(class2[i])
                for i in range(len(class3)):
                    class3.remove(class3[i])

    if o%2!=0:
        for i in range(max(len(class11), len(class22), len(class33))):
            if abs(class11[i]-statistics.mean(class22))>abs(class11[i]-statistics.mean(class11))<abs(class11[i]-statistics.mean(class33)):
                class1.append(class11[i])
            if abs(class22[i]-statistics.mean(class11))>abs(class22[i]-statistics.mean(class22))<abs(class22[i]-statistics.mean(class33)):
                class2.append(class22[i])
            if abs(class33[i]-statistics.mean(class22))>abs(class33[i]-statistics.mean(class33))<abs(class33[i]-statistics.mean(class11)):
                class3.append(class33[i])
        if statistics.mean(class11)==statistics.mean(class1):
            if statistics.mean(class22)==statistics.mean(class2):
                if statistics.mean(class33)==statistics.mean(class3):
                    break
                else:
                    for i in range(len(class11)):
                        class11.remove(class11[i])
                    for i in range(len(class22)):
                        class22.remove(class22[i])
                    for i in range(len(class33)):
                        class33.remove(class33[i])

            else:
                for i in range(len(class11)):
                    class11.remove(class11[i])
                for i in range(len(class22)):
                    class22.remove(class22[i])
                for i in range(len(class33)):
                    class33.remove(class33[i])
        else:
            for i in range(len(class11)):
                class11.remove(class11[i])
            for i in range(len(class22)):
                class22.remove(class22[i])
            for i in range(len(class33)):
                class33.remove(class33[i])