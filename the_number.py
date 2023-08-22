import random

input_number=int(input('Enter the guessed number'))
begin=int(input('Enter the begin number'))
end=int(input('Enter the end number'))
computer=random.randint(begin,end)
matched=0
while  matched<end:
    matched+=1
    if input_number==computer:
        print("Congratulations! You have won")
        break
    elif input_number>computer:
        print('higher! than entered')
        input_number=int(input('Enter the guessed number'))
    elif input_number<computer:
        print("lower! than entered")
        input_number = int (input (' Enter the guess '))
    else:
        print('not ok')
        input_number=int(input('Enter the guessed number'))


