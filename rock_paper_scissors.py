import random

# print('Rock...')
# print('Paper...')
# print('Scissors...')

# player_one = input('Player 1, make your move: ')
# print('--------------\n' * 30)
rand_num = random.randint(0,2)
if rand_num == 0:
    ai = 'rock'
elif rand_num == 1:
    ai = 'paper'
else:
    ai = 'scissors'
print(ai)

# player_two = input('Player 2, make your move: ')
# print('--------------\n' * 30)

   
if player == ai:
    print('Draw')
elif player == 'rock':
    if ai == 'scissors':
        print('Player Wins')
    elif ai == 'paper':
        print('Computer Wins')
elif player == 'paper':
    if ai == 'rock':
        print('Player wins')
    elif ai == 'scissors':
        print('Computer wins')
elif player == 'scissors':
    if ai == 'paper':
        print('Player Wins')
    elif ai == 'rock':
        print('Computer wins')
else:
    print('Something went wrong')
            



