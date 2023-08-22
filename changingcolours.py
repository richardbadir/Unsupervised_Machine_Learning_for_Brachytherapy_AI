import numpy
from PIL import Image
input_image= Image.open("CT49.png")
pixel_map = input_image.load()


width, height = input_image.size
  
for i in range(width//2):
    for j in range(height):
        
        #r, g, b, p = input_image.getpixel((i, j))
          

        #grayscale = (0.299*r + 0.587*g + 0.114*b) #grey

  
        #pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))
        r, g, b, p = input_image.getpixel((i, j))
        pixel_map[i, j] = (int(1*r),int(1*g) , 0*b)
  

input_image.save("halfyellow3", format="png")
  
input_image.show()