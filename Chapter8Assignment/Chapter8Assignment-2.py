filename = input('please enter the file name: ')
try : 
    fhand = open(filename)
except : 
    print(filename, "is incorrect file name")
    quit()
count = 0
for line in fhand :
    line = line.lstrip()
    lst = line.split()
    if len(lst) < 2 :
        continue
    if lst[0] != "From":
        continue
    count = count + 1
    print(lst[1])
print("There were", count, "lines in the file with From as the first word")