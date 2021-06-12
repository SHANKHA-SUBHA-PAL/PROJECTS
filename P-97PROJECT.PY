import random
num = random.randint(1,9)


print('Number Guessing Game')
print('Guess a number between 1 to 9 to win')
chances =0

while chances < 5:
    
    ans = int(input('Enter your guess:'))
    if ans == num:
        print("Congratulations...YOU WON!!!!")
        break
    elif ans<num:
        print("Your guess was too low...")
    else:
        print("Your guess was too high...")

    chances+=1

if chances >=5:
    print("Sorry...You Lost...Better Luck next time")