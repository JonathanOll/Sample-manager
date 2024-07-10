import os
import sys
from json import loads, dumps

options = {}

def options_exists(prog_dir):
    return os.path.exists(prog_dir + "/options.json")

def init_options(prog_dir):
    open(prog_dir + "/options.json", "w+").write("{}")

def verif_options():
    if "open_vscode" not in options : options["open_vscode"] = True

def save_options(prog_dir):
    open(prog_dir + "/options/json").write(dumps(options))

def load_options(prog_dir):
    try:
        s = open(prog_dir + "/options.json", "r").read()
        data = loads(s)
        for k, v in data.items():
            options[k] = v
        return True
    except: return False


def show_options():
    print("Options :")
    for k, v in options.items():
        print("\t- " + str(k) + " : " + str(v))





