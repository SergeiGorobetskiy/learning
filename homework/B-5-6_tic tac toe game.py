# Function for displaying the playing field
def print_field(field):
    print('       -----------        ')
    for i in range(3):
        print('      |', end='')
        for j in range(3):
            print(' ' + field[i][j] + ' |', end='')
        print('\n       -----------')
# Function for checking the winnings
def check_win(field, player):
    for i in range(3):
        if (field[i][0] == player and field[i][1] == player and field[i][2] == player) or \
           (field[0][i] == player and field[1][i] == player and field[2][i] == player):
            return True
        if (field[0][0] == player and field[1][1] == player and field[2][2] == player) or \
           (field[0][2] == player and field[1][1] == player and field[2][0] == player):
            return True
    return False
# Function for checking the possibility of a next step
def check_move(field, x, y):
    if x < 0 or x > 2 or y < 0 or y > 2:
        return False
    if field[x][y] != ' ':
        return False
    return True
# Playing field
field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# The first step 'X'
current_player = 'X'
def check_empty_field(field):
    for i in range(3):
        for j in range(3):
            if field[i][j] == ' ':
                return False
    return True
# Game cycle
print("       Hello player!      ")
print("This is a tic-tac-toe game")
print("The first move is made by X ")
print("   Let's start playing!")
while True:
    print(f"                          Player {current_player} move")
# Output of the playing field
    print_field(field)
# Entering a move
    x = int(input('Enter the line number: ')) - 1
    y = int(input('Enter the column number: ')) - 1
# Checking the possibility of a move
    if check_move(field, x, y):
        field[x][y] = current_player
# Checking for winnings
        if check_win(field, current_player):
# Output of the message
            print_field(field)
            print('Won', current_player)
            print(' End of the game! ')
            break
        if check_empty_field(field):
            print('    Drawn game    ')
            print(' End of the game! ')
            break
# Changing the symbol
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
# Error message output
        print('incorrect move')