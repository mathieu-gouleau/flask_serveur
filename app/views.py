from app import app
from flask import request, redirect
from flask import render_template
import os


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return "<h1 style=' color: red'>About!!!!!!</h1>"
    

@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    
    if request.method == "POST":

        if request.files:

            image = request.files["image"]
            image.save(os.path.join("/Users/NOVASTEP2020/Desktop/APP/app/static/img", image.filename))
            print("image saved")

            return redirect(request.url)


    return render_template("upload_image.html")




