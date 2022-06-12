# numbers and maths

'''print(2 + 4)
print(10 / 3)
print(10 % 3) 
print(2*(3+2)*5**2/4)

# # boys_name= 'david'
# # _no_touchy__

name = 'David'
print(name)
name= 'Daniel'
print(name)


## string concatenation

first_name='David'
last_name='shuaib'
full_name=first_name + ' ' + last_name + ' is the tutor'
print(full_name)


student = 'timi'
print ('The youngest student is ',student)

name='Ali'
name +=' Garuba'
name +=' Ayo'
print(name)


# format method
player= 'seyi'
guesses=8
print(f'{player}\'s guess of {guesses} is wrong')
print(f'my name is {first_name} {last_name}')''''''



#age=int(input('How old are you?\n'))
#print(f'I am {age} years old')


''''''kilo=int(input('How many kilo did you trek today?\n'))

miles = kilo * 0.621371


miles=round(miles,2)

print(f'Your {kilo} km walk is equal to {miles} in miles')'''


## Conditional Logic

'''age=int(input('How old are you?\n'))
if (age<18):
    output=('you are too young to enter the party')

elif(age>=18 and age<21): 
    output=('you can enter but can\'t drink')

elif(age>=21 and age<=65):
    output=('you can enter and drink as well')
else:
    output=('you are too old to party')
print(output)
'


location=input('Where do you live?\'')
if (location== 'mushin'):
    output=('You are a rugged guy')

elif (location== 'ajegunle'):
    output=('You are a rugged guy')

else:
    output=('you live somewhere else')

print(output)''


a='AJEGUNLE'
B='MUSHIN'

city= input('where do you live?|n').upper()
if(city==a or city==b):
    state=('you are a rugged man')

else:
    state=('You live someshere else')

print(state)'''




# Trithiness and Falsiness

'''animal=input('what is your favourite animal')
if animal:
    kayode=(f'{animal} is my favourite too')
else:
    kayode=("Yiu didnt say anything")
print(kayode)'''



#Loops
'''name='muhammed'
for char in name :
    print(char)



for letter in 'coffee':
    print(letter *10)'''

'''for a in range(1,101):
    print(a)

for a in range(0,101):
    print(a)

for a in range(100):
    print(a)'''


'''for num in range(1,11):
    print('\U0001F600' *num)'''



'''for x in range(1,21):
    if(x==4 or x==13):
        state='unlucky'

    elif(x%2 ==0):
        state='Even'

    elif(x%2 !=0):
        state='Odd' 

    else:
        state='Enter a valid number'

    print(f'{x} is {state}')




offense=int(input('how many times have you offended me ?\n'))

for x in range (offense):
    print(f' {x+1} Please forgive me')'''

'''admin=int(input('Admin Enter a Number'))


for num in range(3):
    user=int(input('Enter your guess'))

    if admin == user:
        print(f'Congratulations your guess of {user} is correct')
        break

    elif (admin !=user):
        print(f'oops! your guess of {user} is wrong. you have made {num +1} move(s)')

    else:
        print('Enter a valid number')'''



## While Loop

'''num=2
while num < 12:
    print(num)

    num +=1


password =input('Enter your secret password\n')
while password !='banana':
    print('you are wrong')
    password = input('Enter your secret password\n')
print('correct') '''


'''admin=int(input('Admin Enter a Number'))
num=1
while num <= 3:
      num+=1
      user=int(input('Enter your guess'))

      if admin == user:
        print(f'Congratulations your guess of {user} is correct')
        break

      elif (admin !=user):
        print(f'oops! your guess of {user} is wrong. you have made {num-1} move(s)')

      else:
        print('Enter a valid number')'''





#Random Number

#import random

#rand_number=random.random()

#print(rand_number)

'''
#rand_number=random.randint(100,200)
#print(rand_number)


import random
player_wins=0
computer_wins=0
winning_score=3

while(player_wins<winning_score and computer_wins<winning_score):
    print(f'player score = {player_wins} - Computer Score = {computer_wins}')

    print('...rock...')
    print('...paper...')
    print('..scissors...')

    player=input('Take your move').lower()
    if player=='quit' or player=='q':
        break

    rand_num=random.randint(0,2)
    if rand_num==0:
        computer ='rock'

    elif rand_num==1:
        computer='paper'
    
    else:
        computer='scissors'

    print(f'Computer plays {computer}')

    if computer==player :
        print(" it's a tie ")
    elif player=='rock': 
        if computer=='paper':
            print('Computer wins')
            computer_wins +=1
        else:
            print('Player wins')
            player_wins +=1
    elif player =='paper':
        if computer=='rock':
            print('Player wins')
            player_wins +=1
        else:
            print('Computer wins')
            computer_wins +=1
    elif player == 'scissors':
        if computer=='paper':
            print('player wins')
            player_wins +=1 

        else:
            print('Computer wins')
            computer_wins +=1
    else:
        print('Enter a valid move')

print(f'FINAL SCORE: player = {player_wins} - computer = {computer_wins}')
if player_wins==computer_wins:
    print('ITS A TIE')

elif player_wins> computer_wins:
    print('CONGRATS PLAYER, YOU WON ')

else:
    print('OH NO! THE COMPUTER WON')'''




# python list

student = ["kayode ", "bola" , "john" , "davison"]

print(student)

# array methods

# append

late_come='Ayo'
student.append(late_come)
print(student)

#join

print(','.join(student))


#insert

student.insert(2, 'desmond')

print(student)



# re-assign


name='oladipo'
student[1]=name

print(student)


#to pop

student.pop(2)

print(student)



#extend

fruits=["orange", "mango", "apple", "water melon", "banana","mango"]
cars=["toyota", "lexus","benz","ford"]

fruits.extend(cars)

print(fruits)



cars.extend(fruits)
print(cars)



x=fruits.count('mango')
print(x)



#name='banana'
#y=name.count('a')

#print(y)

z=fruits[4].count('a')
print(z)
#slicing an array
student = ["kayode", "bola" , "john" , "davison"]
print(student[1:3])
#Getting the length of an array
print(len(student))
#Removing an index of an array
student.remove("kayode")
print(student)
#Clearing an array
student.clear()
print(student)
#del student
#print(student)

students = ["Damilola", "David", "Gabriel", "Timileyin", "Daniel"]
student_name=input("What is your name? ").capitalize()
if student_name in students:
    print(f"Welcome to the class {student_name}")
else:
    print(f"{student_name} you are not a part of the class")



count =0

