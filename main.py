from flask import Flask, render_template, send_file, send_from_directory, safe_join, abort, redirect, url_for
from flask_restful import Api, Resource, request
import os, pathlib, datetime

uploads_path = "uploads"
allowed_extensions = [".pdf"]


app = Flask(__name__)
app.config["uploads_path"] = uploads_path
api = Api(app)
THIS_FOLDER = app.root_path

def correct_name(name):
    return (name[-4:] in allowed_extensions)


@app.route("/")
def home():
    return render_template("/index.html")

@app.route("/process", methods=["GET"])
def post_upload():
    return render_template("/upload.html")


@app.route("/api/v1.0/tasks/render/", methods=["POST"])
def upload():
    file = request.files["file"]
    if (correct_name(file.filename)):
        #file.save(os.path.join(app.config["uploads_path"], file.filename[:-4] + "-input.pdf"))
        file.save(os.path.join(THIS_FOLDER, uploads_path, file.filename[:-4] + "-" +str(datetime.datetime.now()).replace(":","-").replace(" ", "") + "-input.pdf"))
    return redirect(url_for('post_upload'))

if __name__ == "__main__":
    app.run(debug=True)
