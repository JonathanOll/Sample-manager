from command import *


class ListCommand(Command):
    def __init__(self, prog_dir, options):
        super().__init__(prog_dir, options)
        self.name = "list"
        self.aliases = ["list", "l", "li"]

    def run(self, args):
        super().run(args)
        print("Samples : ")
        for i in os.listdir(self.prog_dir + "/samples/"):
            print("\t-" + i.lower())
        
        return True



