#4 More list Practice
def removeDuplicates(list):
    uniquelist = []
    for number in list:
        if number not in uniquelist:
            uniquelist.append(number)
    print(uniquelist)

list = [1, 2, 2, 2, 3, 11, 1, 2]
removeDuplicates(list) #debug: first time it deleted the later iterations of the duplicates
