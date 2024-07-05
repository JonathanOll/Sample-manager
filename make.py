import sys
import os
import shutil


def make(args, prog_dir) -> bool:
    try:
        name = args[0]

        target = "./"
        if len(args) > 1 : target = args[1]

        folder = prog_dir + "/samples/" + name

        if not os.path.exists(folder) :
            print("No such sample : " + name)
            return False

        shutil.copytree(folder, target)
        print("Loaded sample " + folder + " in " + target)

        return True
    except: return False

