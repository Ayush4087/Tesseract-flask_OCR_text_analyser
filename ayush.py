import OCR
import os

name = OCR.name_txt
appended_file = name.split(".")[0]+"_appended.txt"
appended_save = os.path.join("ANALYSIS_DATA",appended_file)

obj = open(appended_save,"r")
data = obj.readlines()
print(data)
print(type(data))
obj.close()