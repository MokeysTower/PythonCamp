def ask(t):
    while True:
        try:
            x = float(input(t))
            if x <= 0:
                raise
        except:
            continue
        else: 
            return x


mass = ask('Write your weight (kg)\n')
tall = abs((pow(ask('write your tall (meters)\n'), 2)))
BMI = mass / tall
print('BMI=', mass / tall)
if (BMI < 18.5):
    print('You have underweight')
elif (18.5 <= BMI < 24.9):
    print('normal')
elif (24.9 <= BMI < 29.9): 
    print('overweight')
elif (29.9 <= BMI < 34.9):
    print('obese')
elif (34.9 <= BMI):
    print('extremely obese')