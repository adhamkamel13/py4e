score = input('please enter score between 0.0 - 1.0: ')
try:
    sc = float(score)
except:
    print('please enter a valid value')
    quit()
if sc >= 0.0 :
    if sc <= 1.0:
        if sc >= 0.9 :
            print('A')
        elif sc >= 0.8:
            print('B')
        elif sc >= 0.7:
            print('C')
        elif sc >= 0.6:
            print('D')
        elif sc < 0.6:
            print('F')
    else: 
        print('error please enter a value within the range')
else: 
    print('error please enter a value within the range')
