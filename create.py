import os
import sys
import shutil

def create(args, prog_dir) -> bool:
    try:
        name, folder = args[0], args[1]
        
        os.mkdir(prog_dir + "/samples/" + name)
        shutil.copytree(folder, prog_dir + "/samples/" + name)
        print("Created " + name + " sample in " + prog_dir + "/samples/" + name)

        return True
    except: return False