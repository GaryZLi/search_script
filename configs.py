import os
from memory import modes
from modes import Modes

print("configs")

class Configs:
    def __init__(self):
        self.mode = Modes().RECURSE
        self.results = ''
        self.currentDir = os.path.abspath(os.path.dirname(__file__))
        self.currentArgIndex = 1
        self.ignoreCase = True
        self.ignoreFileCase = True
        self.root = "/Users/garyli/Code/signifyd/platform"
        self.skips = [
            'build',
            '.jpg',
            '.jks',
            '.png',
            '.parquet',
            '.DS_Store',
            'jq',
            '.tar',
            '.pyc',
            '.bin',
            '.jar',
            '.probe',
            '.lock',
            '.class',
            '.zip',
            '.git',
            '.pdf',
            '.model',
            'logglyTrustStore',
        ]
        self.keywords = []
        self.avoidKeywords = set([])
        self.filesInclude = set([])
        self.filesExclude = set([
            'Test.java'
        ])