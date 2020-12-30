import cv2
import numpy as np
from time import sleep


largura_min = 80
altura_min = 80
offset = 6
pos_linha = 550

# FPS do vídeo
delay = 60

detec = []
carros = 0

	
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


# video source input
cap = cv2.VideoCapture('video.mp4')
# OpenCV provides Background Subtraction algorithms.
# we can perform background Subtraction using matrix subtraction, i.e, just subtracting the static frame from the video.
# But this has a lot of drawbacks.
# It is a very less efficient algorithm for Background subtraction because it does not update itself.
# This problem is being handled by the Background Subtraction algorithms provided by OpenCV.
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame1 = cap.read()
    tempo = float(1/delay)
    sleep(tempo) 
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    # The morphologyEx() of the method of the class Imgproc accepts src, dst, op, kernel as parameters
    dilatada = cv2.morphologyEx(dilat, cv2. MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2. MORPH_CLOSE, kernel)

    # OpenCV has findContour() function that helps in extracting the contours from the image.
    # It works best on binary images, so we should first apply thresholding techniques, Sobel edges, etc.
    contorno, h = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # it will create a line
    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255, 127, 0), 3)
    for(i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0, 255), -1)

        for (x, y) in detec:
            if (y < (pos_linha + offset)) and (y > (pos_linha-offset)):
                carros += 1
                cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0, 127, 255), 3)
                detec.remove((x, y))
                print("car is detected : " + str(carros))

    # cv2.putText() method is used to draw a text string on any image.
    # Parameters: image, text, org(coordinate), font, color, thickness
    cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    cv2.imshow("Video Original", frame1)
    cv2.imshow("Detectar", dilatada)

    # To display the image, you can use the imshow() method of cv2
    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
