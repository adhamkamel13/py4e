givenfile = input('please enter the file name : ')
try :
    fhand = open(givenfile)
except :
    print(givenfile, 'is incorrect file name and not exist')
    quit()
count = 0
totnumbers = 0.0
for line in fhand :
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    findindex = line.find(':')
    piece = float(line[findindex+1 :].strip()) #turn the value that after the ":" into float value then rid off fron all the spaces around it
    totnumbers = totnumbers + piece
    count = count + 1 
print('Average spam confidence:', totnumbers/count)