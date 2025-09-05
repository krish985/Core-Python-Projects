import random

print("Welcome to rock,paper,scissors game :)")

# options and tracking scores.
options = ['rock' , 'paper' , 'scissor']
computer_score = 0
user_score = 0

while True :
    user_choice = input("Enter (rock , paper , scissor) or q for quit a game : ").lower()

    if user_choice == 'q' :
        break

    if user_choice not in options :
        print("Please Enter Correct Word try again !\n")
        continue

    # Generate computer choice.
    computer_choice = random.choice(options)

    print(f'Computer choice : {computer_choice}')

    # check for winning condition.
    if user_choice == 'rock' and computer_choice == 'scissor' :
        user_score += 1
        print("User won !\n")
    
    elif user_choice == 'paper' and computer_choice == 'rock' :
        user_score += 1
        print('User Won\n')

    elif user_choice == 'scissor' and computer_choice == 'paper' :
        user_score += 1
        print('User Won\n')
    
    elif user_choice == computer_choice :
        print("Tie....\n")
    else :
        computer_score += 1
        print('Computer Won\n')

# Final result.
print(f"\nFinal Scores:\nComputer score : {computer_score}\nUser score : {user_score}")