from flask import Flask , render_template , request
import os
import pandas as pd
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime


app = Flask(__name__)

os.system("clear.py")

@app.after_request
def add_header(response):
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response




@app.route("/" , methods=["GET","POST"])
def upload_files():
    if request.method=="POST":
        files = request.files.getlist("file")
        #-----------------REMOVING EXISTING FILES FROM DATABASE----------------------------------
        files_database = os.listdir("Database")
        if(len(files_database)>0):
            for file in files_database:
                path = os.path.join("Database",file)
                os.remove(path)
        #-----------------------------------------------------------------------------------------

        for file in files:
            file.save(os.path.join("Database", file.filename))

        
        os.system("OCR.py")
        os.system("Analysis.py")
        os.system("appending_analysis.py")

        li = os.listdir("ANALYSIS_DATA")
        for file in li:
            sp_name = file.split("_")
            if("appended.txt" in sp_name):
                name = file
                break

        path_app = os.path.join("ANALYSIS_DATA",name)
        obj = open(path_app,"r")
        data = obj.readlines()
        obj.close()

        return render_template("upload.html",content=data)
        

    return render_template("upload.html")


if(__name__=="__main__"):
    app.run(host='127.0.0.1',port=8080,debug=True)