import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

from uuid import uuid4


def center(file):
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255 and item[3]==0:
            newData.append((255, 255, 255))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(file.filename, "PNG")

    img = cv2.imread(file.filename,cv2.IMREAD_GRAYSCALE)
    # im = cv2.imread('img3.png',cv2.COLOR_BGR2HSV)

    # Negate image so whites become black 
    img =255-img #beyazlar siyah oldu

    # Find anything not black, i.e. the ball(kullandığımız görüntü)

    nz = cv2.findNonZero(img)    #Sıfır olmayan piksellerin konumlarının listesini döndürür !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1 siyah olmayanların koordinatları

    #print(type(nz))    #output = <class 'numpy.ndarray'>
    #print(nz)


    liste = list()

    for array in nz:
        liste.append(array)

    i=0
    liste_x = list()
    while i < len(liste):

        x_coordinates = liste[i][0][0]
        liste_x.append(x_coordinates)
        i+=1

    #print(liste_x)

    m_x = len(liste_x)

    coor_toplam_x = sum(liste_x)

    x = coor_toplam_x / m_x


    j=0
    liste_y = list()
    while j < len(liste):

        y_coordinates = liste[j][0][1]
        liste_y.append(y_coordinates)
        j+=1

    #print(liste_y)

    m_y = len(liste_y)

    coor_toplam_y = sum(liste_y)

    y = coor_toplam_y / m_y 



    print ("cismin ağırlık merkezi koordinatları:","(" ,x,",", y ,")")

    #print(img.shape)

    image = mpimg.imread(file.filename)


    plt.imshow(image)
    plt.plot(x, y, "o", markersize=10)  # og:shorthand for green circle

    # urn = uuid4()
    plt.savefig('static/upload/a{}'.format(file.filename))
    # print(urn.hex)
    # plt.show()
    
    return x,y