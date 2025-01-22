from load_image import ft_load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io

def main():
    imageArray : np.array = ft_load('animal.jpeg')
    grayScale = Image.fromarray(imageArray[100:100+400, 450:450+400]).convert("L")
    grayArray = np.array(grayScale)
    x = grayArray.reshape((400,400,1))
    print("New shape after slicing:",x.shape, 'or', grayArray.shape)
    print(x)
    img = plt.imshow(x, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()