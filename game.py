import random

name = input('Enter your name: ')
print(f"Hello, {name}")

lst = input()
print("Okay, let's start")

d = {'rock': "paper", 'paper': 'scissors', 'scissors': 'rock'}


#  reading through the lines
rating = open('rating.txt', 'r').readlines()

for line in rating:
    if name in line:
        score = int(line.split()[1])
        #  print("Your rating:", score)
        break
    else:
        score = 0
        

def rps(my_input):
    global score, lst
    
    if len(lst) == 0:
        computer_guess = random.choice(list(d.values()))
    
        if d[my_input] == computer_guess:
            print(f'Sorry, but the computer chose {computer_guess}')
            score = score
        
        elif my_input == computer_guess:
            print(f'There is a draw ({computer_guess})')
            score += 50
        else:
            print(f'Well done. The computer chose {computer_guess} and failed')
            score += 100
    
    elif len(lst) > 0:
        lst1 = lst.split(',')
        ind = lst1.index(my_input)
        lst1 = lst1[ind + 1:] + lst1[:ind]
        computer_guess = random.choice(lst1)
    
        if my_input == computer_guess:
            print(f'There is a draw ({computer_guess})')
            score += 50
        
        elif lst1.index(computer_guess) < len(lst1) / 2:
            print(f'Sorry, but the computer chose {computer_guess}')
            score = score
    
        elif lst1.index(computer_guess) >= len(lst1) / 2:
            print(f'Well done. The computer chose {computer_guess} and failed')
            score += 100
        

def main():
    while True:
        user_input = input()
        if user_input == '!rating':
            #  rating_()
            print("Your rating: ", score)
            
        if user_input in list(d.values()) or user_input in lst:
            rps(user_input)
        
        elif user_input not in ['scissors', 'paper', 'rock'] and user_input not in lst \
                and user_input != '!rating' and user_input != '!exit':
            print("Invalid input!")
        elif user_input == '!exit':
            print("Bye!")
            break
#  rating.close()


main()
