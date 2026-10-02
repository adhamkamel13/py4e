#function to compute pay
def computepay(hours, rate) :
    if hours > 40 :
        pay = 40 * rate + (hours - 40) * rate * 1.5
        return pay
    elif hours <= 40 :
        pay = hours * rate
        return pay
#compute and print user inputs of hours and rate 
hours = input('please enter the number of hours: ')
rate = input('please enter the rate: ')
try :
    hrs = float(hours)
    rt = float(rate)
except :
    print('please enter a valid value:')
    quit()
print('Pay' , computepay(hrs , rt))
