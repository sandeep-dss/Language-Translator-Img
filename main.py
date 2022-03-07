import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
from englisttohindi.englisttohindi import EngtoHindi
import cv2
import matplotlib.pyplot as plt
import numpy as np
from googletrans import Translator

def main():
   
    cap = cv2.VideoCapture(1)
    while cap.isOpened():
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        txt = tess.pytesseract.image_to_string(Image.fromarray(img1))
        cv2.imshow('frame', img1)
        translator =Translator()
        translator.translate(txt, dest='te')

        #res = EngtoHindi(txt)
        print(txt)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            return translator



    cap.release()




if __name__ == "__main__":
 main()

