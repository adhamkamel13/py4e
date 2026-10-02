hours = input('enter hours: ')
try :
    hrs = float(hours)
except :
    hrs = -1
rate = input('enter rate: ')
try :
    rt = float(rate)
except :
    rt = -1
if hrs <= 40 :
    pay = (hrs * rt)
else:
    pay = 40 * rt + ((hrs - 40) * rt * 1.5)
print(pay)