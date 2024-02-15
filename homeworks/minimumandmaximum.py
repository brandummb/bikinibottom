list = [15, 20, 3, 24, 231, 342, 23, 3, 1, 1029]
max = list[0]
min = list[0]
for n in list:
    if min > n+1:
       min = n+1 
    else:
        max = n
print('max = ' + str(max))
print('min = ' + str(min))