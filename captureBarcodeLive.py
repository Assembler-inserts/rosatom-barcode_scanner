
from PIL import Image
from pyzbar.pyzbar import decode
import imutils

import cv2
from time import sleep
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(1)
sleep(2)
while True:

    try:
        check, frame = webcam.read()
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        frame = imutils.resize(frame, width=400)
        barcodes = decode(frame);
        if len(barcodes) >= 1:
            print(barcodes[0].data);
        else:
            print("No bar");
        
        # # loop over the detected barcodes
	# for barcode in barcodes:
		# # extract the bounding box location of the barcode and draw
		# # the bounding box surrounding the barcode on the image
		# (x, y, w, h) = barcode.rect
		# cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		# # the barcode data is a bytes object so if we want to draw it
		# # on our output image we need to convert it to a string first
		# barcodeData = barcode.data.decode("utf-8")
		# barcodeType = barcode.type
		# # draw the barcode data and barcode type on the image
		# text = "{} ({})".format(barcodeData, barcodeType)
		# cv2.putText(frame, text, (x, y - 10),
			# cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		# # if the barcode text is currently not in our CSV file, write
		# # the timestamp + barcode to disk and update the set
		# if barcodeData not in found:
			# csv.write("{},{}\n".format(datetime.datetime.now(),
				# barcodeData))
			# csv.flush()
			# found.add(barcodeData)
        
        
        if key == ord('s'): 
            print("S ok")
            cv2.imwrite(filename='saved_img.jpg', img=frame)
           
            frame = imutils.resize(frame, width=400)
            print(decode(frame).data)
            sleep(1)
            # webcam.release()
            # print("Processing image...")
            # img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            # print("Converting RGB image to grayscale...")
            # gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            # print("Converted RGB image to grayscale...")
            # print("Resizing image to 28x28 scale...")
            # img_ = cv2.resize(gray,(28,28))
            # print("Resized...")
            # img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            # print("Image saved!")
            
            # break
        
        elif key == ord('q'):
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