from PIL import Image

import numpy as np
im = np.array(Image.open('CT49.png'))


print("Before trimming:",im.shape)


im_trim = im[240:400, 128:450]

print("After trimming:",im_trim.shape)


Image.fromarray(im_trim).save('otherhalf_CT49.png')