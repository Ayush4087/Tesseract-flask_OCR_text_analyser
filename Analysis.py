import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import OCR
import os
import shutil

name = OCR.name_txt
file_path = os.path.join("ANALYSIS_DATA",name)
obj = open(file_path,"r")

data = obj.read()
words = data.split()

unique = []
for word in words:
    if word not in unique:
        unique.append(word)

word_count = []
for word in unique:
    word_count.append(words.count(word))

analysis_name = name.split(".")[0]+"_Analysis.txt"
analysis_save = os.path.join("ANALYSIS_DATA",analysis_name)

obj = open(analysis_save,"w+")

for i in range(0,len(unique),1):
    obj.write(unique[i])
    obj.write("   :   ")
    obj.write(str(word_count[i]))
    obj.write("\n")

obj.close()

labels = unique
sizes = word_count

plt.pie(sizes, labels=labels,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')

# plot_name = name.split(".")[0]+"_plot.png"
plot_save = os.path.join("static","plot1.png")

plt.savefig(plot_save, dpi=300, bbox_inches='tight')

files = os.listdir("Database")

for file in files:
    path_from = os.path.join("Database",file)
    path_to = os.path.join("static","uploaded1.png")
    shutil.copy(path_from,path_to)