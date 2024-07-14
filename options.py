from command import *


options = {}

class OptionCommand(Command):
    def __init__(self, prog_dir):
        super().__init__(prog_dir)
        self.name = "options"
        self.aliases = ["options", "opt", "o", "settings", "option", "setting"]

    def run(self, args):
        super().run(args)

    def options_exists(self):
        return os.path.exists(self.prog_dir + "/options.json")

    def init_options(self):
        open(self.prog_dir + "/options.json", "w+").write("{}")

    def verif_options(self):
        if "open_vscode" not in options : options["open_vscode"] = True
        if "connect_to_git" not in options : options["connect_to_git"] = True
        if "git_main_branch" not in options : options["git_main_branch"] = "main"

    def save_options(self):
        open(self.prog_dir + "/options.json", "w").write(dumps(options))

    def load_options(self):
        try:
            s = open(self.prog_dir + "/options.json", "r").read()
            data = loads(s)
            for k, v in data.items():
                options[k] = v
            return True
        except: return False

    def show_options(self):
        print("Options :")
        for k, v in options.items():
            print("\t- " + str(k) + " : " + str(v))





