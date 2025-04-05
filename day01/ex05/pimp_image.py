from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array):
    '''
    Inverts the color of the image received.
    '''
    inverted = 255 - array
    plt.imshow(inverted)
    plt.show()


def ft_red(array):
    '''
     Apply red filter to the image received.
    '''
    cp = np.copy(array)
    for height in cp:
        for pix in height:
            pix[1] = pix[1] * 0
            pix[2] = pix[2] * 0
    plt.imshow(cp)
    plt.show()


def ft_green(array):
    '''
    Apply green filter to the image received.
    '''
    cp = np.copy(array)
    for height in cp:
        for pix in height:
            pix[0] = pix[0] - pix[0]
            pix[2] = pix[2] - pix[2]
    plt.imshow(cp)
    plt.show()


def ft_blue(array):
    '''
    Apply blue filter to the image received.
    '''
    cp = np.copy(array)
    for height in cp:
        for pix in height:
            pix[0] = 0
            pix[1] = 0
    plt.imshow(cp)
    plt.show()


def ft_grey(array):
    '''
    Apply grey filter to the image received.
    '''
    cp = np.copy(array)
    for height in cp:
        for pix in height:
            sum = np.sum([pix[0], pix[1], pix[2]])
            pix[0] = sum / 3
            pix[1] = sum / 3
            pix[2] = sum / 3

    plt.imshow(cp)
    plt.show()


def main():
    imageArray = ft_load('landscape.jpg')
    ft_invert(imageArray)
    ft_red(imageArray)
    ft_green(imageArray)
    ft_blue(imageArray)
    ft_grey(imageArray)


if __name__ == '__main__':
    main()
