from command import *
from options import options

URL_REGEX = re.compile(r"(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?")

class MakeCommand(Command):
    def __init__(self, prog_dir):
        super().__init__(prog_dir)
        self.name = "make"
        self.aliases = ["make", "m"]

    def run(self, args):
        super().run(args)

        if not (1 <= len(args) <= 2) :
            print("Incorrect argument count")
            return False

        try:
            name = args[0]

            target = "./" + name + "/"
            if len(args) > 1 : target = args[1]
            folder = self.prog_dir + "/samples/" + name

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

