#2.1 Part 1
superawesomelist = []
for number in range (0,51): #debug: setting range from (0,50) resulted in the number 50 missing from my list
    superawesomelist.append(number)
#2.2 Part 2
def square(list): #debug: orig. wrote def square(): with no positional arg., resulting in error, had to put square(list) and then worked
    squarelist = []
    for number in superawesomelist:
        squarelist.append(int(number) ** 2)
    print(squarelist)

square(superawesomelist)

#2.3 Part 3
listA = []
for number in range(0,11):
    listA.append(number)
listB = []
for number in range(20,31):
    listB.append(number)
oddorderedlist = []
for number in listA:
    if number % 2 != 0:
        oddorderedlist.append(number)
for number in listB:
    if number % 2 != 0:
        oddorderedlist.append(number)
print(oddorderedlist)