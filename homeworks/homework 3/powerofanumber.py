def powerofanumber():
    x = int(input("base:" ))
    y = int(input("power:" ))
    z = x
    for n in range(1,y):
        x *= z
    print(x)

powerofanumber()