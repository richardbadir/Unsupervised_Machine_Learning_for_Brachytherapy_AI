import numpy as np
import pydicom
from pydicom import dcmread
import matplotlib.pyplot as plt
from pydicom.data import get_testdata_file

# fpath = get_testdata_file("CT49.dcm")

fpath = "/home/sebquet/Desktop/Richard_2022/1194868_Anon/downsampled/CT2_downsampled.dcm"

print(fpath)
ds = dcmread(fpath)
print(ds)


npy_array = ds.pixel_array
print(ds.pixel_array)

print(npy_array.shape)

plt.imshow(npy_array)
plt.show()