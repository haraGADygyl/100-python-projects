weight = int(input('Enter your weight: \n'))
height = int(input('Enter your height: \n'))

height_meters = height / 100
bmi = weight / (height_meters * height_meters)

print(f'Your Body Mass Index is {bmi:.2f}')

if bmi <= 16:
    print('You are severely underweight')
elif bmi <= 18.5:
    print('You are underweight')
elif bmi <= 25:
    print('You are healthy')
elif bmi <= 30:
    print('You are overweight')
else:
    print('You are severely overweight')
