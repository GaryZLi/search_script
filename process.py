from memory import *
import sys

print("process")
print(modes)

# print(app.modes.RECURSE)

# def parseFlags(flag):
#     if flag == '-help':
#         print('-f only check corresponding files using format: fileA/fileB')
#         print('-F check all files')
#         print('-i ignore case')
#         print('-I case sensitive')
#         print('-p starting root path')
#         print('-P starting root path with case senstivity')
#         configs.mode = modes.HELP
#     elif flag == '-i':
#         configs.ignoreCase = True
#     elif flag == '-I':
#         configs.ignoreCase = False
#     elif flag == '-f':
#         files = getNextArg().split('/')
#         for file in files:
#             configs.filesInclude.add(file.lower())
#             if file in configs.filesExclude:
#                 configs.filesExclude.remove(file)
#     elif flag == '-F':
#         configs.ignoreFileCase = False
#         files = getNextArg().split('/')
#         for file in files:
#             configs.filesInclude.add(file)
#             if file in configs.filesExclude:
#                 configs.filesExclude.remove(file)
#     elif flag == '-fA':
#         configs.filesInclude.clear()
#         configs.filesExclude.clear()
#     elif flag == '-p':
#         path = getNextArg()
#         root = path
#     elif flag == '-P':
#         path = getNextArg()
#         root = path
#         configs.ignoreFileCase = False

# def processArg(arg):
#     global configs
#     print("configs.avoidKeywords")


#     if arg[0] == '!':
#         configs.avoidKeywords.add(arg[1:])
#     else:
#         print(configs)
#         configs.keywords.append(arg)

def parseArg(value):
    parsing = value.split('-')

    # arg
    # if len(parsing) == 1:
    #     processArg(value)
    # # -arg
    # elif len(parsing) == 2:
    #     parseFlags(value)
    # else:
    #     print("NOT PARSING: [", value, ']')

# def getArg():
#     return sys.argv[configs.currentArgIndex]

# def getNextArg():
#     configs.currentArgIndex += 1
#     return getArg()
