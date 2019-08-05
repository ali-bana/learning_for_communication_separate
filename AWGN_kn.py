import os
from six.moves import cPickle
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt

def psnr(img1, img2):
    # print(np.square(img1-img2, dtype='int'))
    mse = np.square(img1-img2, dtype='int').mean()
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    r = (PIXEL_MAX**2)/mse
    # print(r, mse)
    return 10 * math.log10(r)





f = open("cifar-10-batches-py/data_batch_1", 'rb')
datadict = cPickle.load(f,encoding='latin1')
f.close()
x = datadict["data"]
y = datadict['labels']
#%%
for snr in [0, 1, 2]:
    psnrs = dict()
    # snr = 1
    n = 32*32*3
    for s in range(5):
        print(s)
        arr = np.array(x[s])
        arr = arr.reshape((3, 32, 32))
        im = [[[0 for __ in range(3)] for _ in range(32)] for ___ in range(32)]

        for i in range(32):
            for j in range(32):
                im[i][j][0] = arr[0][i][j]
                im[i][j][1] = arr[1][i][j]
                im[i][j][2] = arr[2][i][j]
        im = np.array(im)
        image = Image.fromarray(im)
        # image.show()


        i = 0.01
        while i < 0.5:
            r = i * math.log2(1 + snr)
            q = 95
            while(True):
                if q <= 1:
                    if not i in psnrs.keys():
                        psnrs[i] = []
                    psnrs[i].append(14)
                    break
                # image.save('t.png')
                image.save('t.jpg', 'JPEG', quality=q, optimize=False, progressive=False)
                size = os.path.getsize('t.jpg')
                # print(size/n, r)
                # n = os.path.getsize('t.png')
                print(size/n, r)
                if (size/n) <= r:
                    saved_image = Image.open('t.jpg')
                    im1arr = np.asarray(image, dtype='int')
                    im2arr = np.asarray(saved_image, dtype='int')
                    # print()
                    i += 0.01
                    if not i in psnrs.keys():
                        psnrs[i] = []
                    psnrs[i].append(psnr(im1arr, im2arr))
                    break
                q -= 2

            i += 0.05
    plt.plot(list(psnrs.keys()), [np.mean(psnrs[_]) for _ in psnrs.keys()])
    print(len(psnrs[list(psnrs.keys())[0]]))
plt.show()

#%%

print(psnrs[list(psnrs.keys())[5]])
print(np.mean(psnrs[list(psnrs.keys())[5]]))

plt.plot(list(psnrs.keys()), [psnrs[_][1] for _ in psnrs.keys()])
plt.show()