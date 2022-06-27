import os
import sys
import re

class Modes:
    HELP = 'HELP'
    RECURSE = 'RECURSE'

modes = Modes()

root = "/Users/garyli/Code/signifyd/platform"
skips = [
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

keywords = [
]

avoidKeywords = set([
])

filesInclude = set([
])

filesExclude = set([
    'Test.java'
])

ignoreCase = True
ignoreFileCase = True
# ------------------------------------------------------------------------------------------


    # def convertSnakeCaseToEnumCase(self, variable):
    #     result = ''
    #     for char in variable:
    #         if isupper(char):
    #             result += '_'
    #         result += char.upper()
    #     return result

    # def convertToEnum(self):
    #     print(vars(self))
    # def updateConfig(self, ):

# TODO: need to start using this configs
# configs = Configs()

mode = modes.RECURSE
results = ''
currentDir = os.path.abspath(os.path.dirname(__file__))
currentArgIndex = 1

def getArg():
    return sys.argv[currentArgIndex]

def getNextArg():
    global currentArgIndex
    currentArgIndex += 1
    return sys.argv[currentArgIndex]

def parseFlags(flag):
    global ignoreCase
    global root
    global mode
    global ignoreFileCase

    if flag == '-help':
        print('-f only check corresponding files using format: fileA/fileB')
        print('-F check all files')
        print('-i ignore case')
        print('-I case sensitive')
        print('-p starting root path')
        print('-P starting root path with case senstivity')
        mode = modes.HELP
    elif flag == '-i':
        ignoreCase = True
    elif flag == '-I':
        ignoreCase = False
    elif flag == '-f':
        files = getNextArg().split('/')
        for file in files:
            filesInclude.add(file.lower())
            if file in filesExclude:
                filesExclude.remove(file)
    elif flag == '-F':
        ignoreFileCase = False
        files = getNextArg().split('/')
        for file in files:
            filesInclude.add(file)
            if file in filesExclude:
                filesExclude.remove(file)
    elif flag == '-fA':
        filesInclude.clear()
        filesExclude.clear()
    elif flag == '-p':
        path = getNextArg()
        root = path
    elif flag == '-P':
        path = getNextArg()
        root = path
        ignoreFileCase = False

def processArg(arg):
    if arg[0] == '!':
        avoidKeywords.add(arg[1:])
    else:
        keywords.append(arg)

def parse(value):
    parsing = value.split('-')

    # arg
    if len(parsing) == 1:
        processArg(value)
    # -arg
    elif len(parsing) == 2:
        parseFlags(value)
    else:
        print("NOT PARSING: [", value, ']')

def checkDataInFile(path):
    with open(path, 'r') as file:
        global ignoreCase
        
        fileText = file.read().lower() if ignoreCase else file.read()

        for avoidKeyword in avoidKeywords:
            avoidKeyword = avoidKeyword.lower() if ignoreCase else avoidKeyword
            if avoidKeyword in fileText:
                return

        for keyword in keywords:
            keyword = keyword.lower() if ignoreCase else keyword
            if keyword not in fileText:
                return

        global results
        results = results + path + '\n'

def recurse(path):
    if os.path.isdir(path):
        for item in os.listdir(path):
            proceed = True

            for skip in skips:
                if skip in item:
                    proceed = False
                    break

            if proceed:
                recurse(path + '/' + item)
    else:
        global ignoreFileCase
        pathToCheck = path.lower() if ignoreFileCase else path

        for fileInclude in filesInclude:
            proceed = False
            
            if re.search(fileInclude, pathToCheck):
                proceed = True
                break

            if not proceed:
                return
                
        for fileExclude in filesExclude:
            if fileExclude in pathToCheck:
                return

        checkDataInFile(path)

def end(test):
    with open(currentDir + '/results', 'w') as file:
        file.write(results)

        if not test:
            print(results)

def start(test):
    global currentArgIndex
    while currentArgIndex < len(sys.argv):
        arg = sys.argv[currentArgIndex]
        parse(arg)
        currentArgIndex += 1

    if mode == modes.RECURSE:
        recurse(root)
    end(test)

test=False
start(test)