def vowels(string):
    vowelcount = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in string:
        for vowel in vowels:
            if letter is vowel:
                vowelcount += 1
            else:
                continue
    print(vowelcount)


string = input('how many vowels are in ')
vowels(string)