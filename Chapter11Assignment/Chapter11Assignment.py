import re
fname = input("please enter the file name: ")
try:
    fhand = open(fname)
except:
    print(fname, "is incorrect file name, please try again.")
    quit()
readfile = fhand.read()
sum = 0
temp = re.findall('[0-9]+', readfile) # make a list of one or more digit that's in the file using (re library)
for i in temp:
    sum = sum + float(i)
print(sum)