def calculate_bmi():
    mass = float(input('mass: (kg) '))
    height = float(input('height: (m) '))
    BMI = mass / (height ** 2)
    print('ur BMI:' + str(BMI))

calculate_bmi()