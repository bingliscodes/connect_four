## a connect four game for player v player or player v ai ##
from AI_player import *
import random

print("test")
checkers = ['X', 'O']
def display_menu():
    print('Welcome to Connect 4!\n')
    print('(0) Play against another human')
    print('(1) Play against an AI')
    print('(2) Quit')

def play():
    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            connect_four(Player('X'), Player('O'))

        elif choice == 1:
            print('prepare yourself...')
            human_v_ai()
        elif choice == 2:
            break
    print('Have a good day!')


def human_v_ai():
    p1 = Player(random.choice(checkers))
    level = int(input('Select difficulty (0-4):'))
    connect_four(p1, AIPlayer(p1.opponent_checker(), 'RANDOM', level))

play()



    
