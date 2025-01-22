from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main():
    '''
    load "animal.jpeg zoom it and display it
    '''
    imageArray = ft_load('animal.jpeg')
    zoomedImage = Image.fromarray(imageArray[100:100+400, 450:450+400])
    grayArray = np.array(zoomedImage.convert("L"))
    x = grayArray.reshape((400, 400, 1))
    print("New shape after slicing:", x.shape, 'or', grayArray.shape)
    print(x)
    plt.imshow(x, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
