import random

computer = random.randint(1,10)
attempts = 10

for i in range(1,attempts+1):

    user = int(input('Enter a number 1 to 10: '))

    if user < computer:
        print('You choose smaller number')

    elif user > computer:
        print('You choose greater number')
        
    else:
        print('Congrats you choose right option')
        break 
else:
    print('Better Luck Next Time!')