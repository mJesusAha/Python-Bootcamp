import yaml
from yaml import *
from pprint import pprint

with open("../materials/todo.yml") as f:
    templates = yaml.safe_load(f)

dict_file = [
    {
        "hosts": "all",
        "tasks": [
            {
                "ansible.builtin.package": {
                    "name": [
                        templates["server"]["install_packages"][0],
                        templates["server"]["install_packages"][1],
                    ],
                    "update_cache": True,
                    "state": "latest",
                }
            },
            {
                "ansible.builtin.copy": {
                    "dest": "~/ ",
                    "mode": "0777",
                    "src": "{{ sitem }}",
                },
                "with_items": [
                    templates["server"]["exploit_files"][0],
                    templates["server"]["exploit_files"][1],
                ],
            },
            {
                "ansible.builtin.shell": [
                    "python3 " + templates["server"]["exploit_files"][0],
                    "python3 "
                    + templates["server"]["exploit_files"][1]
                    + " -e "
                    + templates["bad_guys"][0]
                    + " "
                    + templates["bad_guys"][1],
                ]
            },
        ],
    }
]

with open(r"deploy.yml", "w") as file:
    documents = yaml.dump(dict_file, file)
