print('Rock...')
print('Paper...')
print('Scissors...')

player_one = input('Player 1, make your move: ')
player_two = input('Player 2, make your move: ')



def play_game():

    play_game = True

    while play_game:
        if player_one == 'rock':
            if player_two == 'scissors':
                print('Player 1 Wins')
            elif player_two == 'paper':
                print('Player 2 wins')
        elif player_one == 'paper':
            if player_two == 'rock':
                print('Player 1 wins')
            elif player_two == 'scissors':
                print('Player 2 wins')
        elif player_one == 'scissors':
            if player_two == 'paper':
                print('Player 1 Wins')
            elif player_two == 'rock':
                print('Player 2 wins')
        elif player_one == player_two:
            print('Draw')
        else:
            print('Something went wrong')
            
        play_game= False

play_game()




# if player_one == 'rock' and player_two == 'scissors':
#     print('Player 1 wins!')
# elif player_one == 'rock' and player_two == 'paper':
#     print('Player 2 wins')
# elif player_one == 'paper' and player_two == 'rock':
#     print('Player 1 wins')
# elif player_one == 'paper' and player_two == 'scissors':
#     print('Player 2 wins')
# elif player_one == 'scissors' and player_two == 'rock':
#     print('Player 2 wins')
# elif player_one == 'scissors' and player_two == 'paper':
#     print('Player 1 wins')
# elif player_one == player_two:
#     print('Draw, Go again')
# else:
#     print('Something went wrong, Please try again')