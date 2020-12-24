import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

# from uuid import uuid4


def center(file):
    imgGet = Image.open(file)
    imgGet = imgGet.convert("RGBA")
    datas = imgGet.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255 and item[3]==0:
            newData.append((255, 255, 255))
        else:
            newData.append(item)

    imgGet.putdata(newData)
    imgGet.save(file.filename, "PNG")

    img = cv2.imread(file.filename,cv2.IMREAD_GRAYSCALE)

    img =255-img #beyazlar siyah oldu

    nz = cv2.findNonZero(img)    
    
    liste = list()

    for array in nz:
        liste.append(array)

    i=0
    liste_x = list()
    while i < len(liste):

        x_coordinates = liste[i][0][0]
        liste_x.append(x_coordinates)
        i+=1

    m_x = len(liste_x)

    coor_toplam_x = sum(liste_x)

    x = coor_toplam_x / m_x


    j=0
    liste_y = list()
    while j < len(liste):

        y_coordinates = liste[j][0][1]
        liste_y.append(y_coordinates)
        j+=1


    m_y = len(liste_y)

    coor_toplam_y = sum(liste_y)

    y = coor_toplam_y / m_y 



    print ("cismin ağırlık merkezi koordinatları:","(" ,x,",", y ,")")


    image = mpimg.imread(file.filename)

    print(file.filename)
    plt.imshow(image)
    plt.plot(x, y, "o", markersize=10)  # og:shorthand for green circle


    plt.savefig('static/upload/a{}'.format(file.filename))
   
    # img =False
    # plt = False
    # image = False
    # imgGet = False
    
    return x,y