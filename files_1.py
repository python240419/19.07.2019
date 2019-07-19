
def printFile(name):
    fileHandler = open(name)

    for line in fileHandler:
        print(line, end="")

    fileHandler.close()

printFile('c:/itay/hello.txt')

print("\n==================")

#f1 = open('c:/itay/hello.txt', 'r+')
#f1.seek(3)
#f1.write("B")

#f1.close()

with open('c:/itay/hello.txt', 'a') as theFile: # theFile = open('c:/itay/hello.txt', 'a')
    theFile.write('more text')
    # theFile.close() -- this is auto added

printFile('c:/itay/hello.txt')
