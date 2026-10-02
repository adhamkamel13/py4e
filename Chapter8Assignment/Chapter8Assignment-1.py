filename = input("please enter the file name: ")
try :
    fhand = open(filename)
except :
    print(filename , "is incorrect file name")
    quit()
mainlist = list()
for line in fhand :
    line = line.lstrip()
    words = line.split()
    for word in words :
        if not word in mainlist :
            mainlist.append(word)
mainlist.sort()
print(mainlist)
    