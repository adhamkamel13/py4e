fname = input("please enter the file name: ")
try :
    fhand = open(fname)
except :
    print(fname,"is incorrect file name, please try again.")
    quit()
dic = dict()
bigstring = None
bigvalue = None
for line in fhand :
    line = line.lstrip()
    words = line.split()
    if len(words) < 2 or words[0] != "From" :
        continue
    dic[words[1]] = dic.get(words[1],0) + 1
for word,count in dic.items() :
    if bigvalue is None or bigvalue < count:
        bigvalue = count
        bigstring = word
print(bigstring, bigvalue)