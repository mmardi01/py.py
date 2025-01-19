from numpy import array
import numpy as np
from PIL import Image
import PIL as pil


def ft_load(path: str) -> array:
    '''
    loads an image, prints its format, and its pixels
    content in RGB format.
    '''
    try:
        image = Image.open(path)
        x = np.array(image)
        print(x.shape)
        return x
    except FileNotFoundError:
        print("File not found")
    except pil.UnidentifiedImageError:
        print('File is not an image')
    except Exception:
        print("Failed to read file")
