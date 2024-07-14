import sys
import os
import shutil
import re
from json import loads, dumps


class Command:
    DEBUG = True
    def __init__(self, prog_dir, options):
        self.prog_dir = prog_dir
        self.name = "command"
        self.aliases = []
        self.options = options
    
    def run(self, args):
        if Command.DEBUG:
            print("running", self.name, "with args", args)