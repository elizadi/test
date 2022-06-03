import numpy as np
import matplotlib.pyplot as plt
import cv2

grayImage = r'D:/documents/test/cv/gray_image.jpg'
colourImage = r'D:/documents/test/cv/colour_image.jpg'

I_gray = cv2.imread(grayImage, cv2.IMREAD_GRAYSCALE)        
I_BGR = cv2.imread(colourImage)

plt.imshow(I_gray, cmap = 'gray')
plt.imshow(I_BGR[:,:,::-1])

I_gray_resized = cv2.resize(src = I_gray, fx = 2, fy = 0.5, dsize = None)       #change size of image

plt.imshow(I_gray_resized, cmap = 'gray')       #output image
plt.xticks([])                                  #output x-axis
plt.yticks([])                                  #output y-axis

I_gray_resized.shape                            #output size of resized image
I_gray.shape                                    #output size of image


I_BGR_resized = cv2.resize(src = I_BGR, fx = 2, fy = 2, dsize = None)           #change size of image

plt.imshow(I_BGR_resized[:,:,::-1])
plt.xticks([])
plt.yticks([])

I_gray_resized = cv2.resize(src = I_gray, fx = 0.5, fy = 0.5, dsize = None)

plt.imshow(I_gray_resized, cmap = 'gray')
plt.xticks([])
plt.yticks([])

I_gray_resized.shape
I_gray.shape

I_BGR_resized = cv2.resize(src = I_BGR, fx = 2, fy = 2, dsize = None)

plt.imshow(I_BGR_resized[:,:,::-1])
plt.xticks([])
plt.yticks([])

numRows = I_gray.shape[0]
numCols = I_gray.shape[1]

print(numRows, numCols)

plt.imshow(I_gray, cmap = 'gray')

I_gray2 = np.zeros((numRows, numCols), dtype = 'uint8')

plt.imshow(I_gray2, cmap = 'gray')

for i in range(int(numRows/2)):     
    for j in range(numCols):
        I_gray2[i, j] = I_gray[i, j]
        
plt.imshow(I_gray2, cmap = 'gray')

I_gray3 = np.zeros((numRows, numCols), dtype = 'uint8')

plt.imshow(I_gray3, cmap = 'gray')

for i in range(numRows):                        #output inver y-axis image
    for j in range(numCols):
        I_gray3[i, numCols - j - 1] = I_gray[i, j]
        
plt.imshow(I_gray3, cmap = 'gray')

S = np.array([[2, 0], [0, 2]])

I2 = np.zeros((2*numRows, 2*numCols), dtype = 'uint8')      #create a dark monochromatic image

for i in range(numRows):                        #overlate a dark monochromatic image on original image
    for j in range(numCols):
        P = np.array([i, j])
        P_dash = S.dot(P)
        new_i, new_j = P_dash[0], P_dash[1]
        I2[new_i, new_j] = I_gray[i, j]
        
plt.imshow(I2, cmap = 'gray')
print(I2.shape)

import matplotlib as mpl
def displayImageInActualSize(I):               #function for output image in actual size
    dpi = mpl.rcParams['figure.dpi']
    H, W = I.shape
    figSize = W/float(dpi), H/float(dpi)
    fig = plt.figure(figsize = figSize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.imshow(I, cmap = 'gray')
    plt.show

displayImageInActualSize(I2)                    #output image in actual size
