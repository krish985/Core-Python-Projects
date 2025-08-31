print("Welcome to quize game :- ")

answer = input("Are you Really want to play that game (y/n) : ").lower()

if answer != 'y' :
    quit()

print('Okayy then move ahaed :) ') 
score = 0

# question 1.
answer = input('CPU stands from ? ').lower()
if answer == 'central processing unit' :
    print('Correct!')
    score += 1
else :
    print('Incorrect')


# question 2.
answer = input('GPU stands from ? ').lower()
if answer == 'graphical processing unit' :
    print('Correct!')
    score += 1
else :
    print('Incorrect')


# question 3.
answer = input('RAM stands from ? ').lower()
if answer == 'random access memory' :
    print('Correct!')
    score += 1
else :
    print('Incorrect')

# question 4.
answer = input('OS stands from ? ').lower()
if answer == 'operating system' :
    print('Correct!')
    score += 1
else :
    print('Incorrect')

# printing result.
print("you score : " + str(score) + "/4")
print(f"Your percentage is : {(score / 4) * 100}%")



