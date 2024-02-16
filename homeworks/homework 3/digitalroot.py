def digital_root(integer):
    sum = 0
    number = str(integer)
    for digits in number:
        sum += int(digits)
    print('digital root = ' + str(sum))

integer = input('digital root? ' )
digital_root(integer)

