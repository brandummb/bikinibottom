def max_forloop(list):
    maximum = list[0]
    for number in list:
        if maximum < number:
            maximum = number
        else:
            continue
    print('max = ' + str(maximum))

def max_whileloop(list):
    maximum = list[0]
    counter = 0
    while counter + 1 < len(list):
        if maximum < list[counter]:
            maximum = list[counter]
        else:
            maximum = maximum
        counter += 1          
    print('max = ' + str(maximum))

def min_forloop(list):
    minimum = list[0]
    for number in list:
        if minimum > number:
            minimum = number
        else: 
            minimum = minimum
    print('min = ' + str(minimum))

def min_whileloop(list):
    minimum = list[0]
    counter = 0
    while counter + 1 < len(list):
        if minimum > list[counter]:
            minimum = list[counter]
        else:
            minimum = minimum
        counter +=1
    print('min = ' + str(minimum))


list = [1, 5, 12, 342, 3, 234, 23]
max_forloop(list)
max_whileloop(list)
min_forloop(list)
min_whileloop(list)