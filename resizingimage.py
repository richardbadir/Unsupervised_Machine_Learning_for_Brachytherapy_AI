import numpy as np
from PIL import Image
load_img_rz = np.array(Image.open('CT49.png').resize((1000,1000)))

Image.fromarray(load_img_rz).save('r_CT49.png')

print("After resizing:",load_img_rz.shape)