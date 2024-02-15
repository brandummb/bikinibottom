def rotate_digits(number):
    import math
    lastdigit = number - int(number / 10) * 10
    number = lastdigit * (10 ** (int(math.log(number)) + 1)) + int(number/10)

number = int(input('number: '))
rotate_digits(number)
print(number)


