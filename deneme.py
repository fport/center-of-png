from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def center(file):
    img = Image.open(file)
    img_mtx = img.load()
    top = bottom = 0
    first_row = True

    # First we find the top and bottom border of the object
    for row in range(img.size[0]):
        for col in range(img.size[1]):
            if img_mtx[row, col][0:3] != (255, 255, 255):
                bottom = row
                if first_row:
                    top = row
                    first_row = False
    middle_row = (top + bottom) / 2  # Calculate the middle row of the object

    left = right = 0
    first_col = True

    # Scan through the middle row and find the left and right border
    for col in range(img.size[1]):
        if img_mtx[middle_row, col][0:3] != (255, 255, 255):
            left = col
            if first_col:
                right = col
                first_col = False
    middle_col = (left + right) / 2  # Calculate the middle col of the object

    print(middle_row, middle_col)

    image = mpimg.imread(file)

    plt.imshow(image)
    plt.plot(middle_row, middle_col, "o", markersize=10)
    # plt.show()

        


    plt.savefig('static/upload/{}'.format(file.filename))
    plt.close()

    return (middle_row+0.5),(middle_col+0.5)
