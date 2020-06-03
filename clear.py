import os



folder_name = "ANALYSIS_DATA"

num = os.listdir(folder_name)

if(len(num)>0):
    for file in num:
        path = os.path.join(folder_name,file)
        os.remove(path)

folder_name = "static"

num = os.listdir(folder_name)

if(len(num)>0):
    for file in num:
        path = os.path.join(folder_name,file)
        os.remove(path)

print("Directory has been cleared !!!")