range = input('Enter a range for guessing a number  :- ')

if range.isdigit() :
    range = int(range);
else :
    print("Print Number Again !")
    quit()

# generate a random number.
import random

random_val = random.randint(0 , range)

score = 0    # it tracks score.

while True :
    guess = int(input("Guess a number :) "))
    
    # special condition.
    if guess > range :
        score = score + 1
        print("Upper Bound")
        continue;
    elif guess < 0 :
        score = score + 1
        print('Lower bound')
        continue;
    
    if guess == random_val :
        score = score + 1
        break;
    elif guess < random_val :
        score = score + 1;
        print("Predict higher number !")
    elif guess > random_val :
        score = score + 1
        print("Pedict lower number !")

# winning statement.
print(f"Congrats you won the game your score is {score}")
        


