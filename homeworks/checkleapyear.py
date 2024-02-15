year = int(input('Leap Year? '))
if int(year / 400) - year / 400 == 0 :
    print('yup')
elif int(year / 100) - year / 100 :
    print('nah')
elif int(year / 4 ) - year/4 :
    print('yup')
else:
    print('nope')