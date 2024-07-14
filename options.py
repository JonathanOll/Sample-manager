from command import *

class Options:
    def __init__(self, prog_dir):
        self.options = {}
        self.prog_dir = prog_dir
    
    def init(self):
        if not os.path.exists(self.prog_dir + "/options.json"):
            open(self.prog_dir + "/options.json", "w+").write("{}")
        else:
            if not self.load() : return False
        
        self.verif()
        self.save()

        return True

    def load(self):
        try:
            s = open(self.prog_dir + "/options.json", "r").read()
            data = loads(s)
            for k, v in data.items():
                self.options[k] = v
            return True
        except: return False

    def get(self, opt):
        return self.options.get(opt)

    def put(self, key, val):
        print("set",key,val)
        self.options[key] = val
        self.save()
    
    def verif(self):
        if "open_vscode" not in self.options : self.options["open_vscode"] = True
        if "connect_to_git" not in self.options : self.options["connect_to_git"] = True
        if "git_main_branch" not in self.options : self.options["git_main_branch"] = "main"
    
    def save(self):
        open(self.prog_dir + "/options.json", "w").write(dumps(self.options))
        print("saving to", self.prog_dir + "/options.json")
    
    def show(self):
        print("Options :")
        for k, v in self.options.items():
            print("\t- " + str(k) + " : " + str(v))


class OptionCommand(Command):
    def __init__(self, prog_dir, options):
        super().__init__(prog_dir, options)
        self.name = "options"
        self.aliases = ["options", "opt", "o", "settings", "option", "setting"]

    def run(self, args):
        super().run(args)
        if len(args) == 0:
            self.options.show()
        elif len(args) == 2:
            self.options.put(args[0], args[1])
        
        return True

    def options_exists(self):
        return 

    def init_options(self):
        open(self.prog_dir + "/options.json", "w+").write("{}")





