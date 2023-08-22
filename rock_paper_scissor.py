# Here, using random and random.choice along with if, elif, and else conditions
import random
hand=['rock','paper','scissor']
computer=['rock','paper','scissor']
def player_choice():
    human=random.choice(hand)
    machine=random.choice(computer)
    if (human=='rock' and machine == 'scissor') or  (human=='paper' and machine=='rock') or (human=='scissor' and machine=='paper'):
        print(f"""{human}  {machine}""")
        print('human won')
    elif(human=='rock' and machine=='rock') or   (human=='paper' and machine=='paper') or (human=='scissor' and machine=='scissor'):
        print(f"""{human}  {machine}""")
        print('draw')
    else:
        print(f"""{human}  {machine}""")
        print('computer won')

player_choice()
