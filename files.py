f1 = open('c:/itay/hello.txt')

for line in f1.readlines():
    print(line, end="")

print("\n==================")

f1.seek( 3 )

for line in f1.readlines():
    print(line, end="")

f1.close()

