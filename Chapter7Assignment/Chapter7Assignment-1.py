givenfile = input('please enter the file name: ')
try : 
    fhand = open(givenfile)
except : 
    print(givenfile ,'is incorrect file name')
    quit()
data = fhand.read()
upperdata = data.upper()
print(upperdata)