# http://127.0.0.1:8888/?specie=Time%20Lord&?species=Sontaran
# http://127.0.0.1:8888/?species=Time%20Lord&?species=Sontaran
# curl 'http://127.0.0.1:8888/?species=Time%20Lord'
# curl -G -d 'species=Dalek' http://127.0.0.1:8888/
# curl http://127.0.0.1:8888/

from wsgiref.util import setup_testing_defaults, request_uri
from wsgiref.simple_server import make_server
from urllib.parse import urlparse, parse_qs


def search_form(dict_url_parse):
    dict_exempl_form = {
        "Cyberman": "John Lumic",
        "Dalek": "Davros",
        "Judoon": "Shadow Proclamation Convention 15 Enforcer",
        "Human": "Leonardo da Vinci",
        "Ood": "Klineman Halpen",
        "Silence": "Tasha Lem",
        "Slitheen": "Coca-Cola salesman",
        "Sontaran": "General Staal",
        "Time Lord": "Rassilon",
        "Weeping Angel": "The Division Representative",
        "Zygon": "Broton",
    }
    if len(dict_url_parse) == 0 or dict_url_parse.get("species") == None:
        return '{"credentials": "Unknown"}', 0
    return search_from_exampl_form(dict_exempl_form, dict_url_parse.get("species"))


def search_from_exampl_form(dict_exempl_form, form):
    for_credentials = ""
    counter_none = 0
    count_i = 0
    for i in range(len(form)):
        if dict_exempl_form.get(form[i]) == None:
            counter_none += 1
        else:
            count_i = count_i + 1
            if count_i > 1 and i < (len(form)):
                for_credentials = for_credentials + ", "
            for_credentials = for_credentials + dict_exempl_form.get(form[i])
    if counter_none == len(form):
        return '{"credentials": "' + "Unknown" + '"' + "}", 0
    return '{"credentials": "' + for_credentials + '"' + "}", 1


def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    url_parse = urlparse(request_uri(environ))
    dict_url_parse = parse_qs(url_parse[4])
    return_ = search_form(dict_url_parse)
    status = "404 Not found"
    if return_[1] == 1:
        status = "200 OK"
    start_response(status, [("Content-Type", "application/json")])
    return [return_[0].encode("UTF-8")]


if __name__ == "__main__":
    port = 8888
    with make_server("", port, simple_app) as httpd:
        print("Слушает порт", port, "...")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down.")
            httpd.server_close()
