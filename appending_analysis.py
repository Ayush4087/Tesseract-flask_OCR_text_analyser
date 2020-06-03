import os
import OCR
import Analysis

name = OCR.name_txt
file_path = os.path.join("ANALYSIS_DATA",name)
obj = open(file_path,"r")

data1 = obj.read()
obj.close()

analysis_name = name.split(".")[0]+"_Analysis.txt"
analysis_save = os.path.join("ANALYSIS_DATA",analysis_name)

obj = open(analysis_save,"r")
data2 = obj.read()

obj.close()

appended_file = name.split(".")[0]+"_appended.txt"
appended_save = os.path.join("ANALYSIS_DATA",appended_file)
obj = open(appended_save,"w+")
obj.write("Extracted Text\n")
obj.write("----------------------------------------\n")
obj.write(data1)
obj.write("\n----------------------------------------")
obj.write("\n")
obj.write("Data Analysis\n")
obj.write("----------------------------------------\n")
obj.write(data2)
obj.close()