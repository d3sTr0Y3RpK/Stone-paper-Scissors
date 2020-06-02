import time
import sys
import random


def win():
    print('GAME: You win.')

def lost():
    print('GAME: You lost.')

def draw():
    print('GAME: Its a draw.')


def game():

    moves = ['stone', 'paper', 'scissors']

    print('GAME: stone, Paper, Scissors?')
    attempts = 4
    while True:
        if attempts == 0:
            print('GAME: You failed to provide a correct option to play the game. please try again.')
            time.sleep(3)
            sys.exit(0)

        player = str(input('Player: ')).lower()
        if player.lower() not in moves:
            print(f'GAME: Invalid Option! You have {attempts} attempts left.')
            attempts -= 1
        else:
            computer = random.choice(moves)
            print(f'Computer: {computer}')

            if player == computer:
                draw()
            elif player == 'stone' and computer == 'scissors':
                win()
            elif player == 'stone' and computer == 'paper':
                lost()
            elif player == 'paper' and computer == 'stone':
                win()
            elif player == 'paper' and computer == 'scissors':
                lost()
            elif player == 'scissors' and computer == 'paper':
                win()
            elif player == 'scissors' and computer == 'stone':
                lost()
            else:
                pass

            play_again = str(input('GAME: Retry? (y/n): '))
            if play_again.lower() == 'y':
                game()
            elif play_again.lower() == 'n':
                print('GAME: Game Over. Goodbye.')
                time.sleep(2.5)
                sys.exit(0)
            else:
                print('GAME: Invalid Options. Goodbye.')
                time.sleep(2.5)
                sys.exit(0)


if __name__=='__main__':
    game()
