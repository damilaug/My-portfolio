from unicodedata import name


print(2 + 4)
print(2 + 3.2)
print(10 / 3)
print(10 // 3)
print(10 ** 3)

name = 'David'
print(name)

first_name = 'David'
last_name = 'peter'
full_name = first_name + ' ' + last_name
print(full_name)
print(f'my name is {first_name} {last_name}')

student = 'Timi'
print('the youngest student is', student)
print('the youngest student is' + student)
print('the youngest student is ' + student)

name = 'Ali'
name += ' Garuba'
print(name)

player = 'Gabriel'
guesses = 8

print(f'{player}\'s guess of {guesses} is wrong')

#age = int(input('How old are you ?\n'))
#print(f'I am {age} years old')

#distance = int(input('How many Kilometers have you walked today ?\n'))
#result =   distance / 0.621371
#results = round(result,2)
#print(f'I have walked {results} miles today')


#age = int(input('how old are you ?\n'))
#if(age<18):
#    output = ('you are too young to enter the party')

#elif(age>=18 and age<21):
#    output = ("you can enter but can't drink")

#elif(age>=21 and age<65):
#    output = ('you can enter and drink as well')

#else:
#    output = ('you are too old to party')

#print(output)


#location = input("where do you live ?/n")
#if(location=='Mushin'):
#    output = ('you are a rugged guy')

#elif(location=='shomolu'):
#    output = ('you are fairly rugged')

#else:
#    output = ('you are a correct guy')

#print(output)


for numbers in range(1,21):
    print(numbers)
    if(numbers==1 or numbers==13):
        print('unlucky')
    elif(numbers%2 ==0):
        print('even')
    else:
        print('odd')
    
#number=10
#for player in range(3):
#    guess = int(input('What is your guess?\n'))
#    if(guess==number):
#        print('Congratulations, you got it right')
#        break
#    elif(guess!=number):
#        print("That's a wrong guess \n You have two more chances")
#    elif(guess!=number):
#        print("You've lost the game")
import random
player_win=0
computer_win=0
winning_score=3

while (player_win < winning_score and computer_win < winning_score):
    print(f"player_win={player_win} - computer_win = {computer_win}")
    print('...Rock...')
    print('...Paper...')
    print('...Scissors...')
    player=input('Make your move').lower()
    rand_num=random.randint(0,2)
    if rand_num==0:
        computer="Rock"
    elif rand_num==1:
        computer="Paper"
    else:
        computer="Scissors"

    print(f'Computer player{computer}')

    if computer==player:
        print("It's a tie")
    elif player=="Rock":
        if computer=="Paper":
            print("Computer wins")
            computer_win +=1
        else:
            print("player wins")
            player_win +=1
    elif player=="Paper":
        if computer=="Rock":
            print("Player wins")
            player_win +=1
        else:
            print("Computer wins")
            computer_win +=1
    elif player=="Scissors":
        if computer=="Paper":
            print("Player wins")
            player_win +=1
        else:
            print("Computer wins")
            computer_win +=1
    else:
        print("Enter a valid move")
print(f"Final Score: Player = {player_win} - Computer{computer_win}")