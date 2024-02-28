#3.1 Part 1
fivebyfive = []
for multiples in range(0,5):
    sublist = []
    for number in range(1,6):

        sublist.append(number + (5 * multiples)) #debug: kept getting "'list' object attribute 'append' is read only" because i wrote "sublist.append = [object]"
    fivebyfive.append(sublist)
print(fivebyfive) #debug: list kept returning "[[5], [10], [15], [20], [25]]" because my command: sublist = [] was within my second for loop

#3.2 Part 2
for list in fivebyfive:
    for number in list:
        if number % 3 == 0:
            divby3s = list.index(number)
            list[divby3s] = '?'
print(fivebyfive)
