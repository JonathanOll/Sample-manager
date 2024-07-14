import sys
import os
from json import load, dump

from create import CreateCommand
from make import MakeCommand
from options import OptionCommand


# sample create xxxx ./  : crée/met à jour un template du nom de xxxx, en se basant sur le dossier ./
# sample list : liste les templates existances
# sample make xxxx : crée dans le dossier courant un projet basé sur le template xxxx
# sample remove xxxx : supprime le template xxxx
# sample options xxxx abcd : donne la valeur abcd à l'option xxxx



args = sys.argv[1:]
prog_dir = "/".join(os.path.abspath(__file__).replace("\\", "/").split("/")[:-1])
samples_folder = prog_dir + "/samples/"

commands = [MakeCommand(prog_dir), CreateCommand(prog_dir)]

def clean(args):
    for i in range(len(args)):
        args[i] = args[i].replace("\\", "/").replace('"', "")

def setup():
    os.mkdir(prog_dir + "/samples/")
    return True

def list_samples() -> list:
    res = []
    for i in os.listdir(samples_folder):
        res.append(i.lower())
    return res 

def exists(sample : str) -> bool:
    return sample.lower() in list_samples()

def fatal_error(error=""):
    print("FATAL ERROR : " + error)

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

    

    if not os.path.exists(prog_dir + "/samples/"):
        if not setup() : fatal_error("FATAL ERROR : COULD NOT CREATE FOLDER" + samples_folder)
    if not options_exists(prog_dir) :
        init_options(prog_dir)
    else:
        if not load_options(prog_dir) : fatal_error("FATAL ERROR : COULD NOT LOAD OPTIONS")

    verif_options()
    save_options(prog_dir)

    if len(args) == 0:
        show_usage()
        sys.exit()

    for cmd in commands:
        if args[0].lower() in cmd.aliases:
            if not cmd.run(args[1:]):
                fatal_error()
                sys.exit()




    
    if len(args) == 1 and args[0].lower() in ("options", "option", "opt"):
        show_options()
    elif args[0].lower() == "list":
        print("Existing samples : ")
        for i in list_samples():
            print("\t - " + i)
    elif args[0].lower() == "create":
        create(args[1:], prog_dir)
    elif args[0] in ("options", "option", "opt") and len(args) == 3:
        options[args[1]] = args[2]
        save_options(prog_dir)
    else:
        show_usage()


























