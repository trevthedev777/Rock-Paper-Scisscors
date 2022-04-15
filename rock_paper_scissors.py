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

   
# if player_one == player_two:
#     print('Draw')
# elif player_one == 'rock':
#     if player_two == 'scissors':
#         print('Player 1 Wins')
#     elif player_two == 'paper':
#         print('Player 2 wins')
# elif player_one == 'paper':
#     if player_two == 'rock':
#         print('Player 1 wins')
#     elif player_two == 'scissors':
#         print('Player 2 wins')
# elif player_one == 'scissors':
#     if player_two == 'paper':
#         print('Player 1 Wins')
#     elif player_two == 'rock':
#         print('Player 2 wins')
# else:
#     print('Something went wrong')
            



