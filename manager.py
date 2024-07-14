import sys
import os
from json import load, dump

from create import CreateCommand
from make import MakeCommand
from options import OptionCommand, Options
from list import ListCommand


# sample create xxxx ./  : crée/met à jour un template du nom de xxxx, en se basant sur le dossier ./
# sample list : liste les templates existances
# sample make xxxx : crée dans le dossier courant un projet basé sur le template xxxx
# sample remove xxxx : supprime le template xxxx
# sample options xxxx abcd : donne la valeur abcd à l'option xxxx



args = sys.argv[1:]
prog_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-1])
samples_folder = prog_dir + "/samples/"

options = Options(prog_dir)
commands = [
                MakeCommand(prog_dir, options), 
                CreateCommand(prog_dir, options), 
                OptionCommand(prog_dir, options),
                ListCommand(prog_dir, options)
            ]



def clean(args):
    for i in range(len(args)):
        args[i] = args[i].replace("\\", "/").replace('"', "")

def setup():
    os.mkdir(prog_dir + "/samples/")
    return True

def fatal_error(error=""):
    print("FATAL ERROR : " + error)
    sys.exit()

def show_usage():
    print("Usage : ")
    print("sample create xxxx ./  : crée/met à jour un template du nom de xxxx, en se basant sur le dossier ./")
    print("sample | sample list : liste les templates existances")
    print("sample make xxxx : crée dans le dossier courant un projet basé sur le template xxxx")
    print("sample remove xxxx : supprime le template xxxx")
    print("sample options : liste les options")
    print("sample options xxxx abcd : donne la valeur abcd à l'option xxxx")



if __name__ == "__main__":

    clean(args)
    if not options.init(): fatal_error("Could not init options file")
    
    if len(args) == 0:
        show_usage()
        sys.exit()

    for cmd in commands:
        if args[0].lower() in cmd.aliases:
            if not cmd.run(args[1:]):
                fatal_error()
            sys.exit()
    
    show_usage()


























