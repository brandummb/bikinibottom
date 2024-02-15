list = [15, 20, 3, 24, 231, 342, 23, 3, 1, 1029]
max = list[0]
min = list[0]
for number in list:
    if min > number + 1:
       min = number + 1 
    else:
        max = number
print('max = ' + str(max))
print('min = ' + str(min))