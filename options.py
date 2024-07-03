import os
import sys
from json import loads

options = {}

def init_options(prog_dir):
    open(prog_dir + "/options.json", "w+").write("{}")

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





