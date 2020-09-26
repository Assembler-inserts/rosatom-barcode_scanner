import array as arr

from PIL import Image
from pyzbar.pyzbar import decode
import imutils

import cv2
from time import sleep
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
sleep(2)

#detection threshold from 1 to 99
detectionThreshold = 20;

barcodeRates = {}

onBoardContainer = "nooo";

def onBoardContainerSet(container):
    global onBoardContainer
    if onBoardContainer != container:
        onBoardContainer = container
        print("Container:"+container)
        

while True:
    try:
        check, frame = webcam.read()
        key = cv2.waitKey(1)
        barcodes = decode(frame);
        # if len(barcodes) >= 1:
            # print(barcodes[0].data);
        # else:
            # print("No bar");
        
        # loop over the detected barcodes
        
        # decrement common rate
        for barcodeRate in barcodeRates:
            if barcodeRates[barcodeRate] >= 1:
                barcodeRates[barcodeRate] -= 1;      
        
        #print("Barcodes:[");
        for barcode in barcodes:
            #change barcode rate
            try:
                if barcodeRates[barcode.data] < 100 :
                    barcodeRates[barcode.data] += 2
            except:
                #print("ex")
                barcodeRates[barcode.data] = 1
            
            #print(barcode.data);
            # extract the bounding box location of the barcode and draw
            # the bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # the barcode data is a bytes object so if we want to draw it
            # on our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        if len(barcodeRates) > 0:
            list_d = list(barcodeRates.items())
            list_d.sort(key=lambda i: i[1])
            if list_d[len(list_d)-1][1] > detectionThreshold:
                #print(list_d[len(list_d)-1][0])
                onBoardContainerSet(list_d[len(list_d)-1][0].decode("utf-8"))
                
            else:
                #No container removed
                onBoardContainerSet("No container")
                
                
                #print("No container")
            
        #print(barcodeRates)
        #print("]");
        cv2.imshow("Capturing", frame)
        
        if key == ord('q'): 
            webcam.release()
            cv2.destroyAllWindows()
            break
    
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break