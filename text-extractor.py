import cv2
import os
import pytextractor
from configparser import ConfigParser

#    O Orientation and script detection (OSD) only
#    1 Automatic page segmentation with OSD.
#    2 Automatic page segmentation, but no OSD, or OCR.
#    3 Fully automatic page segmentation, but no OSD. (Default)
#    4 Assume a single column of text of variable sizes.
#    5 Assume a single uniform block of vertically aligned text.
#    6 Assume a single uniform block of textJ
#    7 Treat the image as a single text line.
#    8 Treat the image as a single word.
#    9 Treat the image as a single word in a circle.
#    10 Treat the image as a single character.
#    11 Sparse text. Find as much text as possible in no particular order.
#    12 Sparse text with OSD.
#    13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract—specific.

class TVTextRecognition:

    def __init__(self):
        config = ConfigParser()
        config.read("config.ini")

        #Datos

        self.path           = config["opencv"]['path']
        self.fileName       = config["opencv"]['fileName']
        self.filePath       = None
        self.fileSaveName   = config["opencv"]['fileSaveName']

        self.config         = config["tesseract"]['config']
        self.detect         = config["tesseract"]['detect']

    def main(self):
        try:
            path = self.path
            fileName = self.fileName
            filePath = os.path.join(path, f"{fileName}")
            fileSaveName = self.fileSaveName
            fileSavePath = os.path.join(path, f"{fileSaveName}")
            code = cv2.COLOR_BGR2GRAY
            myconfig = self.config #r"--psm 7 --oem 3" #--psm 6/7/10/11/13 --oem 3
            flag = False
            mylist = self.detect.split(",")


            blob = cv2.imread(filePath)
            frame = cv2.cvtColor(blob, code)
            frame_height, frame_with = frame.shape[:2]
            cv2.imwrite(fileSavePath, frame)


            extractor = pytextractor.PyTextractor()
            text_from_image = extractor.get_image_text(fileSavePath, config=myconfig)


            for ele_arr in text_from_image:
                for ele_list in mylist:
                    if ele_list.lower() in ele_arr.lower() or ele_arr.strip().lower() == ele_list.lower():
                        flag = True
                        break
                    else:
                        continue
                if flag:
                    break
            
            if flag == True:
                print("switch")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            return 0
    
if __name__ == "__main__":
    TVTextRecognition().main()