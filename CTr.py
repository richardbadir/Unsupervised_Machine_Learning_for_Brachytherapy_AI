import pyRad.CT
import pyRad.CoordinateSystem
from pyRad.CT import CT
from pyRad.CoordinateSystem import CoordinateSystem
from pydicom import dcmread


files=["/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT1.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT2.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT3.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT4.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT5.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT6.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT7.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT8.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT9.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT10.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT11.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT12.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT13.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT14.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT15.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT16.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT17.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT18.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT19.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT20.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT21.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT22.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT23.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT24.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT25.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT26.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT27.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT28.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT29.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT30.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT31.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT32.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT33.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT34.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT35.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT36.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT37.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT38.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT39.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT40.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT41.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT42.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT43.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT44.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT45.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT46.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT47.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT48.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT49.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT50.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT51.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT52.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT53.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT54.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT55.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT56.dcm"]

h=[]
for f in range(len(files)):
    h.append(dcmread(files[f]))

m=[]
for j in range(len(h)):
    m.append(h[j].SliceLocation)


attrs= {
"num_voxels": [512, 512, 56],
"spacing": [0.9179688, 0.9179688, 3],
"img_pos":[-275, -407.5, 22.969482],
"slice_coordinates":m,
"slice_flipped":False,
"orient":[-1,1,1]}


l=CoordinateSystem(attrs)

attr = {
"ct_folder": "/home/sebquet/Desktop/Richard_2022/1194868_Anon",
"num_voxels": [512, 512, 56],
"spacing": [0.9179688, 0.9179688, 3],
"img_pos":[-275, -407.5, 22.969482],
"name":"N/A",
"id":1194868,
"orientation":[1, 0, 0, 0, 1, 0],
"rescale_slope":1.0,
"rescale_intercept":0.0,
"slice_coordinates":m,
"coords":l,
"files":["/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT1.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT2.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT3.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT4.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT5.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT6.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT7.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT8.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT9.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT10.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT11.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT12.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT13.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT14.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT15.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT16.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT17.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT18.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT19.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT20.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT21.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT22.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT23.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT24.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT25.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT26.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT27.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT28.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT29.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT30.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT31.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT32.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT33.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT34.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT35.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT36.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT37.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT38.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT39.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT40.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT41.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT42.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT43.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT44.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT45.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT46.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT47.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT48.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT49.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT50.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT51.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT52.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT53.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT54.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT55.dcm", "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT56.dcm"],
}


This_CT= CT(attr)
print("-------------------------------- fet file list ------------------------------")
print("-------------------------------- fet file list ------------------------------")


v=This_CT.files
s=[]
for j in v:
    s.append("/home/sebquet/Desktop/Richard_2022/1194868_Anon/"+j)
print(s)
attr["files"]=s
print(attr["files"])

# print(This_CT.get_slice(4))
#This_CT.downsample_ct(1/3)
# print(This_CT.get_unscaled_grid())
# print(This_CT.slice_from_z(53))
# print(This_CT.as_dict())