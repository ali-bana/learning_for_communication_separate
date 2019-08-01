from six.moves import cPickle
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
f = open("cifar-10-batches-py/data_batch_1", 'rb')
datadict = cPickle.load(f,encoding='latin1')
f.close()
x = datadict["data"]
y = datadict['labels']

#%%
print(len(x[0]))
# print(y)
arr = np.array(x[1])
print(y[0])
print(arr[0], arr[1024], arr[2048])
arr = arr.reshape((3, 32, 32))
im = [[[0 for __ in range(3)] for _ in range(32)] for ___ in range(32)]
#%%
for i in range(32):
    for j in range(32):
        im[i][j][0] = arr[0][i][j]
        im[i][j][1] = arr[1][i][j]
        im[i][j][2] = arr[2][i][j]
im = np.array(im)
img = np.array(im)
# print(image.shape)
image = Image.fromarray(img)

i = 10
while i < 95:
    image.save(str(i)+'.jpg', "JPEG", quality=i, optimize=True, progressive=True)

    i += 10
image.show()



