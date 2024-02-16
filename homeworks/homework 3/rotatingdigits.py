def rotate_digits():
    import math
    number = int(input('number: '))
    lastdigit = number - (int(number / 10) * 10)
    number = lastdigit * (10 ** (int(math.log(number, 10)))) + int(number/10)
    print(number)

rotate_digits()


