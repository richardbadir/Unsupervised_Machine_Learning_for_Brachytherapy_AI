import numpy as np
import pydicom
from pydicom import dcmread
import matplotlib.pyplot as plt
from pydicom.data import get_testdata_file

# fpath = get_testdata_file("CT49.dcm")

fpath = "/home/sebquet/Desktop/Richard_2022/1194868_Anon/CT54.dcm"


ds = dcmread(fpath)


mon_array_numpy = ds.pixel_array
from PIL import Image
input_image= Image.open(ds.pixel_array)

pixel_map = input_image.load()


width, height = input_image.size
  
for i in range(width//2):
    for j in range(height):
        
        #r, g, b, p = input_image.getpixel((i, j))
          

        #grayscale = (0.299*r + 0.587*g + 0.114*b) #grey

  
        #pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
        r, g, b, p = input_image.getpixel((i, j))
        pixel_map[i, j] = (int(1*r),int(1*g) , 0*b)
  

input_image.save("halfyellow2", format="png")
  
input_image.show()