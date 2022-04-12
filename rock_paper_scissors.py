print('Rock...')
print('Paper...')
print('Scissors...')

player_one = input('Player 1, make your move: ')
player_two = input('Player 2, make your move: ')

if player_one == 'rock' and player_two == 'scissors':
    print('Player 1 wins!')
elif player_one == 'rock' and player_two == 'paper':
    print('Player 2 wins')
elif player_one == 'paper' and player_two == 'rock':
    print('Player 1 wins')
elif player_one == 'paper' and player_two == 'scissors':
    print('Player 2 wins')
elif player_one == 'scissors' and player_two == 'rock':
    print('Player 2 wins')
elif player_one == 'scissors' and player_two == 'paper':
    print('Player 1 wins')
elif player_one == player_two:
    print('Draw, Go again')
else:
    print('Something went wrong, Please try again')