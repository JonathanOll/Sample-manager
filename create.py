import os
import sys
import shutil

def create(args, prog_dir) -> bool:
        name, folder = args[0], args[1]
        dest = prog_dir + "/samples/" + name
        
        if os.path.exists(dest) : os.rmdir(dest)
        shutil.copytree(folder, dest)
        print("Created " + name + " sample from " + folder + " to " + dest)

        return True