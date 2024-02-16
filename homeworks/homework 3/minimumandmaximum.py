def minimum_and_maximum(list):
    max = list[0]
    min = list[0]
    for number in list:
        if min > number:
           min = number
        if max < number:
            max = number
    minmax = (min, max)
    print(minmax)

list = [34, 8, 19, 200, 3, 4]
minimum_and_maximum(list)