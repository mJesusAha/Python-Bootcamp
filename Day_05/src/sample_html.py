# Coздание шаблонов
import os
from datetime import datetime
import random


def html_sample():
    if not os.path.isdir("templates"):
        os.mkdir("templates")
    base_file = open("templates/base.html", "+w")
    base_file.write(
        "<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{% block title %}{% endblock %}</title>\n"
    )
    base_file.write(
        "\t</head>\n\t<body>\n\t\t{% block content %}{% endblock %}\n\t</body>\n</html>"
    )
    base_file.close()

    index_file = open("templates/index.html", "+w")
    index_file.write(
        '{% extends "base.html" %}\n\n{% block title %}Home{% endblock %}\n\n'
    )
    index_file.write(
        "{% block content %}\n\t<a href='/'>Обновить</a>\n\t<h2>Music</h2>\n"
    )

    index_file.write(
        '\n\t<form action = "/success", method = "post" enctype="multipart/form-data">'
    )
    index_file.write(
        '\n\t<input type="file" name="file" style="color:red"/> <br /><br />'
    )
    index_file.write(
        '\n\n\t<input type="submit" value="Upload" style="color:red" /></form>'
    )

    index_file.write("\t<ul>\n\t\t{% for music in music_list %}\n")
    index_file.write(
        '\t<form action = "/button", method = "post" enctype="multipart/form-data"><br /><br /><input type="submit" value={{music}} name="file"/></form>\n'
    )
    index_file.write("\t\t{% endfor %}\n\t</ul>")

    index_file.write("\n{% endblock %}")
    index_file.close()

    success_html = open("templates/success.html", "+w")
    success_html.write("<html>\n<head>\n<title>success</title>\n</head>\n")
    success_html.write(
        '<body>\n<a href="/">Назад</a><p>File uploaded successfully</p>\n'
    )
    success_html.write("</body>\n<html>")
    success_html.close()

    unsuccess_html = open("templates/unsuccess.html", "+w")
    unsuccess_html.write("<html>\n<head>\n<title>success</title>\n</head>\n")
    unsuccess_html.write(
        '<body>\n<a href="/">Назад</a><p>Non-audio file detected</p>\n'
    )
    unsuccess_html.write("</body>\n<html>")
    unsuccess_html.close()


def conv():
    t = (str(datetime.now())).replace(" ", "")[-6:-1] + str(random.randint(0, 100))
    try:
        for name in os.listdir("./melody"):
            if name.endswith(".ogg"):
                os.system(
                    f"cd melody\n ffmpeg -i {name} -vn -ar 44100 -ac 2 -b:a 192k {name}{t}.mp3 \n rm -rf {name}"
                )

    except:
        print("не конвентировалось нет приложения ffmpeg")
