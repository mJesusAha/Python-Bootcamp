# python3 -m venv venv    - создание виртуального окружения
# source venv/bin/activate   - активация
# python3 server.py   - загрузка сервера
# pip freeze > requirements.txt   - coздание файла requirements.txt
# python -m pip install -r requirements.txt   - запустить
from flask import Flask, render_template, request
import os
from sample_html import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    html_sample()

    if not os.path.isdir("melody"):
        os.mkdir("melody")
    music_list = os.listdir("./melody")
    new_list_music = set()

    for i in music_list:
        if i.endswith(".mp3") or i.endswith(".wav") or i.endswith(".ogg"):
            new_list_music.add(i)

    if len(request.args) > 0:
        # print ('****', list(request.args)[0]=='loadlist', len(request.args))
        if list(request.args)[0] == "playlist":
            return [list(new_list_music)]

    return render_template("index.html", music_list=new_list_music)


@app.route("/button", methods=["POST"])
def button():
    if request.method == "POST":
        f = request.form["file"]
        file = "./melody/" + f
        os.system("afplay " + file)
        return index()


@app.route("/success", methods=["POST"])
def success():
    if request.method == "POST":
        f = request.files["file"]
        if (
            f.filename.endswith(".mp3")
            or f.filename.endswith(".wav")
            or f.filename.endswith(".ogg")
        ):
            f.save("./melody/" + f.filename)
            print("address", request.files["file"])
            conv()

            return render_template("success.html", name=f.filename)
    return render_template("unsuccess.html", name=f.filename)


if __name__ == "__main__":
    app.run(port=8888)
