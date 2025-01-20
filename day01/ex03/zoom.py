from load_image import ft_load
import numpy as np
from PIL import Image

def main():
    imageArray : np.array = ft_load('animal.jpeg')
    grayScale = Image.fromarray(imageArray).convert('L')
    # grayScale.show()
    x = np.array(grayScale)
    print(x.shape)
    print(x)
    return

if __name__ == "__main__":
    main()