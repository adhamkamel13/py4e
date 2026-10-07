fname = input("please enter the file name: ")
try:
    fhand = open(fname)
except:
    print(fname, "is incorrect file name, please try again.")
    quit()
lst = list()
dic = dict()
for line in fhand:
    line = line.strip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    for word in words:
        if ":" in word:
            strsplit = word.split(":")
            dic[strsplit[0]] = dic.get(strsplit[0], 0) + 1
for k,v in sorted([(k,v) for k,v in dic.items()]):
    print(k,v)