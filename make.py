import sys
import os
import shutil
import re
from options import options

URL_REGEX = re.compile(r"(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?")

def make(args, prog_dir) -> bool:
    try:
        name = args[0]

        target = "./"
        if len(args) > 1 : target = args[1]
        folder = prog_dir + "/samples/" + name

        if os.path.exists(target):
            print(target + " already exists")
            return False
        
        if not os.path.exists(folder) :
            print("No such sample : " + name)
            return False


        if options.get("connect_to_git"):
            print("(leave blank if you don't want to connect to a git)")
            rep = input("Git rep. link  : ")

            if URL_REGEX.match(rep) :
                os.system("git clone " + rep + " " + target)
        print("Git repository initialized")
        

        shutil.copytree(folder, target, dirs_exist_ok=True)
        print("Loaded sample " + folder + " in " + target)

        if options.get("open_vscode"):
            os.system("code " + target)

        print("Done!")
        return True
    except: return False

