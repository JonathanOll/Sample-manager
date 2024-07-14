from command import *


class CreateCommand(Command):
        def __init__(self, prog_dir, options):
                super().__init__(prog_dir, options)
                self.name = "create"
                self.aliases = ["create", "cr", "c"]
        
        def run(self, args):
                super().run(args)

                if not (len(args) == 2) :
                        print("Incorrect argument count")
                        return False

                try:
                        name, folder = args[0], args[1]
                        dest = self.prog_dir + "/samples/" + name
                        
                        if os.path.exists(dest) : os.rmdir(dest)
                        shutil.copytree(folder, dest)
                        print("Created " + name + " sample from " + folder + " to " + dest)

                        return True
                except: return False
