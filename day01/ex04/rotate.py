from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def transpose(arr: list):
    '''
    take an array and return a transposed version of it
    '''
    res = np.zeros([arr[0].__len__(), arr.__len__(), 1], dtype=int)
    for i in range(arr.__len__()):
        for k in range(arr[0].__len__()):
            res[k][i] = arr[i][k]
    return res


def main():
    '''
    load "animal.jpeg zoom it and display rotated version of it
    '''
    imageArray = ft_load('animal.jpeg')
    zoomedImage = Image.fromarray(imageArray[100:100+400, 450:450+400])
    grayArray = np.array(zoomedImage.convert("L"))
    x = grayArray.reshape((400, 400, 1))
    print(x)
    x = transpose(x)
    print(x)
    print("New shape after slicing:", x.shape, 'or', grayArray.shape)
    plt.imshow(x, cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()
