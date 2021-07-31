# DİKKAT!! 2 ADET GLOBAL DEĞİŞKEN BULUNMAKTADIR. GRİD FONKSİYONUNUN İÇİNDE "yanlilik_x" ve "yanlilik_y"

import cv2 
import numpy as np
import os

def grid(disp_X,disp_Y):

    global yanlilik_x
    global yanlilik_y
    
    disp_X += yanlilik_x +85
    disp_Y += yanlilik_y -0

    cv2.line(image,(((disp_X//2)-(w//2)),0),(((disp_X//2)-(w//2)),disp_Y),(0,255,0),1)             #Dikey çizgiler
    cv2.line(image,(((disp_X//2)+(w//2)),0),(((disp_X//2)+(w//2)),disp_Y),(255,0,255),1)

    xXx = (0,((disp_Y//2)+(h//2)))
    yYy = (disp_X,((disp_Y//2)+(h//2)))

    cv2.line(image, (0,((disp_Y//2)-(h//2))), (disp_X,((disp_Y//2)-(h//2))) ,(255,0,255),1)          #Yatay çizgiler
    cv2.line(image, xXx, yYy ,(0,255,0),1)
    
    #cv2.line(image,(0,2*k_Y),(disp_X,2*k_Y),(0,0,0),1)

    """
    cv2.line(image,(k_X,0),(k_X,disp_Y),(0,0,0),1)      #Dikey çizgiler
    cv2.line(image,(2*k_X,0),(2*k_X,disp_Y),(0,0,0),1)

    cv2.line(image,(0,k_Y),(disp_X,k_Y),(0,0,0),1)      #Yatay çizgiler
    cv2.line(image,(0,2*k_Y),(disp_X,2*k_Y),(0,0,0),1)
    """
def stabilize(x,y,k_X,k_Y,disp_X,disp_Y):
    bos_X = k_X//2
    bos_Y = k_Y//2

    if x<disp_X//2 - bos_X:
        print("""
        
       ***
      ****
     ************
    ***************
     ************
      ****
       ***
        
    """)
    if x>disp_X//2 + bos_X:
        print("sagda")
    if y<disp_Y//2 - bos_Y:
        print("yukarida")
    if y>disp_Y//2 + bos_Y:
        print("asagida")
    os.system("cls")
    """
        **
       ***
      ****
     **********
    ***********
     **********
      ****
       ***
        **
    """
def ms_planer():
    pass
cam = cv2.VideoCapture(0)


yanlilik_x = 0
yanlilik_y = 0 

while 1:
    check, image = cam.read()

    disp_X, disp_Y = image.shape[1],image.shape[0]
    k_X = disp_X//3
    k_Y = disp_Y//3

    blur = cv2.GaussianBlur(image,(13,13),0)

    #hsv=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    """lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])"""

    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    #thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]
    #hsv  = cv2.bilateralFilter( hsv , 9 , 75 , 75 )

    #hsv  =  cv2.medianBlur ( hsv , 5 )

    #hsv = cv2.fastNlMeansDenoisingColored(hsv,None,10,10,7,21)


    """çekirdek = cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5))

    hsv  =  cv2.morfolojiEx( image ,  cv2 . MORPH_GRADIENT ,  çekirdek )"""
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)


    
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    MAX = 0
    ret_contour = 0
    if len(contours) != 0:
        # draw in blue the contours that were founded
        #cv2.drawContours(image, contours, -1, 255, 3)

        # find the biggest countour (c) by the area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        
        merkez_X =int(x+(w/2))
        merkez_Y = int(y+(h/2))

        cv2.circle(image,(merkez_X, merkez_Y),int(w/2),(255,0,255),3)
        stabilize(merkez_X, merkez_Y, k_X,k_Y,disp_X,disp_Y)        #havuza yönelme komutları


    ms_planer()

    grid(disp_X,disp_Y)
    


    cv2.imshow("image", image)
    cv2.imshow("lölö",mask)
    k = cv2.waitKey(20) & 0xFF
    if k == 13:
        break
