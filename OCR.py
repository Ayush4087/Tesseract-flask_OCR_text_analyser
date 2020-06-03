from PIL import Image
import pytesseract
import os

name_arr = os.listdir("Database/")
name = name_arr[0]
file_name = os.path.join("Database/",name)

img = Image.open(file_name)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\amishra3\AppData\Local\Continuum\anaconda3\Lib\site-packages\Tesseract-OCR\tesseract'
text = pytesseract.image_to_string(img,lang='eng')

name_txt = name.split(".")[0]+".txt"
path = os.path.join("ANALYSIS_DATA",name_txt)

obj = open(path,"w+")
obj.write(text)
obj.close()

print("DONE :)")