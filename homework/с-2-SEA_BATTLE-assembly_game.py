import os
from random import randrange
from random import choice

class FieldPart(object):
    main = 'map'
    radar = 'radar'
    weight = 'weight'

# set colors.
class Color:
    yellow2 = '\u001b[33m'
    reset = '\u001b[38m'
    blue = '\u001b[34m'
    yellow = '\u001b[33m'
    red = '\u001b[31m'
    miss = '\u001b[30m'

# function that colors text
def set_color(text, color):
    return color + text + Color.reset

# set both the visual display of cells and their color
class Cell(object):
    empty_cell = set_color('0', Color.yellow2)
    ship_cell = set_color('■', Color.blue)
    destroyed_ship = set_color('X', Color.red)
    damaged_ship = set_color('□', Color.red)
    miss_cell = set_color('T', Color.miss) # '•' looks more beautiful

# The playing field consists of three parts:
# 1-map where the player's ships are dropped.
# 2-radar on what moves and results the players have
# 3-field with cells, used for AI moves
class Field(object):

    def __init__(self, size):
        self.size = size
        self.map = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.radar = [[Cell.empty_cell for _ in range(size)] for _ in range(size)]
        self.weight = [[1 for _ in range(size)] for _ in range(size)]

    def get_field_part(self, element):
        if element == FieldPart.main:
            return self.map
        if element == FieldPart.radar:
            return self.radar
        if element == FieldPart.weight:
            return self.weight

# Draw the field. Here is a drawing of a divider into two parts
    def draw_field(self, element):

        field = self.get_field_part(element)
        weights = self.get_max_weight_cells()
# drawing weight for debugging
        if element == FieldPart.weight:
            for x in range(self.size):
                for y in range(self.size):
                    if (x, y) in weights:
                        print('\033[1;32m', end='')
                    if field[x][y] < self.size:
                        print(" ", end='')
                    if field[x][y] == 0:
                        print(str("" + ". " + ""), end='')
                    else:
                        print(str("" + str(field[x][y]) + " "), end='')
                    print('\033[0;0m', end='')
                print()
# draw field
        else:
            for x in range(-1, self.size):
                for y in range(-1, self.size):
                    if x == -1 and y == -1:
                        print("  ", end="")
                        continue
                    if x == -1 and y >= 0:
                        print(y + 1, end=" ")
                        continue
                    if x >= 0 and y == -1:
                        print(Game.letters[x], end='')
                        continue
                    print(" " + str(field[x][y]), end='')
                print("")
        print("")

# Function checks, if the ship is placed on a specific position of a specific field
# will be used when placing ships, as well as when calculating the weight of cells
# False if it won't fit and True if the ship will fit

    def check_ship_fits(self, ship, element):

        field = self.get_field_part(element)

        if ship.x + ship.height - 1 >= self.size or ship.x < 0 or \
                ship.y + ship.width - 1 >= self.size or ship.y < 0:
            return False

        x = ship.x
        y = ship.y
        width = ship.width
        height = ship.height

        for p_x in range(x, x + height):
            for p_y in range(y, y + width):
                if str(field[p_x][p_y]) == Cell.miss_cell:
                    return False

        for p_x in range(x - 1, x + height + 1):
            for p_y in range(y - 1, y + width + 1):
                if p_x < 0 or p_x >= len(field) or p_y < 0 or p_y >= len(field):
                    continue
                if str(field[p_x][p_y]) in (Cell.ship_cell, Cell.destroyed_ship):
                    return False

        return True

# when the ship is destroyed, you need to mark all the cells around (Cell.miss_cell)
# all cells of the ship - destroyed (Cell.destroyed_ship)
    def mark_destroyed_ship(self, ship, element):

        field = self.get_field_part(element)

        x, y = ship.x, ship.y
        width, height = ship.width, ship.height

        for p_x in range(x - 1, x + height + 1):
            for p_y in range(y - 1, y + width + 1):
                if p_x < 0 or p_x >= len(field) or p_y < 0 or p_y >= len(field):
                    continue
                field[p_x][p_y] = Cell.miss_cell

        for p_x in range(x, x + height):
            for p_y in range(y, y + width):
                field[p_x][p_y] = Cell.destroyed_ship

# adding a ship mark these cells on the field like element
# here we pass which part of the field we are accessing:
    # 1-main
    # 2-radar
    # 3-weight
    def add_ship_to_field(self, ship, element):

        field = self.get_field_part(element)

        x, y = ship.x, ship.y
        width, height = ship.width, ship.height

        for p_x in range(x, x + height):
            for p_y in range(y, y + width):
                field[p_x][p_y] = ship

# function returns a list of coordinates with the highest hit chance coefficient
    def get_max_weight_cells(self):
        weights = {}
        max_weight = 0
# cells are entered into a dictionary with a key that is the value in the cell
# remember the maximum value
# take from the dictionary a list of coordinates with the maximum value weights[max_weight]
        for x in range(self.size):
            for y in range(self.size):
                if self.weight[x][y] > max_weight:
                    max_weight = self.weight[x][y]
                weights.setdefault(self.weight[x][y], []).append((x, y))

        return weights[max_weight]

# cell weight recalculation
    def recalculate_weight_map(self, available_ships):
# step 1 - set all cells to 1
# weight effect does not accumulate from turn to turn
        self.weight = [[1 for _ in range(self.size)] for _ in range(self.size)]

# checking the fields
# шf the ship is wounded - put the cells higher, lower and on the sides
# coefficients multiplied by 50 to take into account the position in one of the parties
# diagonals from the wounded cell are zeros
        for x in range(self.size):
            for y in range(self.size):
                if self.radar[x][y] == Cell.damaged_ship:

                    self.weight[x][y] = 0

                    if x - 1 >= 0:
                        if y - 1 >= 0:
                            self.weight[x - 1][y - 1] = 0
                        self.weight[x - 1][y] *= 50
                        if y + 1 < self.size:
                            self.weight[x - 1][y + 1] = 0

                    if y - 1 >= 0:
                        self.weight[x][y - 1] *= 50
                    if y + 1 < self.size:
                        self.weight[x][y + 1] *= 50

                    if x + 1 < self.size:
                        if y - 1 >= 0:
                            self.weight[x + 1][y - 1] = 0
                        self.weight[x + 1][y] *= 50
                        if y + 1 < self.size:
                            self.weight[x + 1][y + 1] = 0

# Checking enemy ships.
# If the ship is destroyed or damaged, or a cell with a miss, the coefficient is 0. Go to the next cell.
# Сheck if this ship can start in any direction from this cell, and if it fits, add coefficient 1 to the cell.

        for ship_size in available_ships:

            ship = Ship(ship_size, 1, 1, 0)
            for x in range(self.size):
                for y in range(self.size):
                    if self.radar[x][y] in (Cell.destroyed_ship, Cell.damaged_ship, Cell.miss_cell) \
                            or self.weight[x][y] == 0:
                        self.weight[x][y] = 0
                        continue
# move the ship around and check if it fits
                    for rotation in range(0, 4):
                        ship.set_position(x, y, rotation)
                        if self.check_ship_fits(ship, FieldPart.radar):
                            self.weight[x][y] += 1

class Game(object):
    letters = ("A", "B", "C", "D", "E", "F")
    ships_rules = [1, 1, 1, 1, 2, 2, 3]
    field_size = len(letters)

    def __init__(self):

        self.players = []
        self.current_player = None
        self.next_player = None

        self.status = 'prepare'

# At the start of the game, we assign the current and next player
    def start_game(self):

        self.current_player = self.players[0]
        self.next_player = self.players[1]

# Status switching function
    def status_check(self):
# switch from prepare to in game if two players are added to the game
# next start the game

        if self.status == 'prepare' and len(self.players) >= 2:
            self.status = 'in game'
            self.start_game()
            return True
# switch to game over status if the next player has 0 ships left
        if self.status == 'in game' and len(self.next_player.ships) == 0:
            self.status = 'game over'
            return True

    def add_player(self, player):
# when adding a player, create a field for him
        player.field = Field(Game.field_size)
        player.enemy_ships = list(Game.ships_rules)
# arrange ships
        self.ships_setup(player)
 # calculate the weight for the cells of the field, this is only needed for AI
        player.field.recalculate_weight_map(player.enemy_ships)
        self.players.append(player)

    def ships_setup(self, player):
# do the placement of ships according to the rules specified in the Game class
        for ship_size in Game.ships_rules:
# set the number of attempts when placing ships randomly
#  needed in order not to get into an infinite loop when there is very little space left for the last ship
            retry_count = 50

# create a preliminary ship-blank
            ship = Ship(ship_size, 0, 0, 0)

            while True:

                Game.clear_screen()
                if player.auto_ship_setup is not True:
                    player.field.draw_field(FieldPart.main)
                    player.message.append('Where to put {} ship '.format(ship_size))
                    for _ in player.message:
                        print(_)
                else:
                    print('') # can display a message
                    # '{}. Setting up ships...Please wait '.format(player.name)

                player.message.clear()

                x, y, r = player.get_input('ship_setup')
# if the user entered some nonsense, the function will return zeros, so we do continue
# just ask you to enter the coordinates again
                if x + y + r == 0:
                    continue

                ship.set_position(x, y, r)

# if the ship is placed at a given position - add a ship to the player on the field
# also add the ship to the player's ship list. and move on to the next ship for placement
                if player.field.check_ship_fits(ship, FieldPart.main):
                    player.field.add_ship_to_field(ship, FieldPart.main)
                    player.ships.append(ship)
                    break

# if the ship does not fit. we write to the user that the position is incorrect
# and we take away the attempt to arrange
                player.message.append('Wrong position!')
                retry_count -= 1
                if retry_count < 0:
# after a given number of unsuccessful attempts - reset the player's card
# remove all the ships and start the arrangement on a new
                    player.field.map = [[Cell.empty_cell for _ in range(Game.field_size)] for _ in
                                        range(Game.field_size)]
                    player.ships = []
                    self.ships_setup(player)
                    return True

    def draw(self):
        if not self.current_player.is_ai:
            self.current_player.field.draw_field(FieldPart.main)
            self.current_player.field.draw_field(FieldPart.radar)
# to know the weight of the cells can be commented/uncommented
# self.current_player.field.draw_field(FieldPart.weight)
        for line in self.current_player.message:
            print(line)

# function for players change
    def switch_players(self):
        self.current_player, self.next_player = self.next_player, self.current_player

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


class Player(object):

    def __init__(self, name, is_ai, skill, auto_ship):
        self.name = name
        self.is_ai = is_ai
        self.auto_ship_setup = auto_ship
        self.skill = skill
        self.message = []
        self.ships = []
        self.enemy_ships = []
        self.field = None

# placement of ships (input_type == "ship_setup")
# making a shot (input_type == "shot")
    def get_input(self, input_type):

        if input_type == "ship_setup":

            if self.is_ai or self.auto_ship_setup:
                user_input = str(choice(Game.letters)) + str(randrange(0, self.field.size)) + choice(["H", "V"])
            else:
                user_input = input().upper().replace(" ", "")

            if len(user_input) < 3:
                return 0, 0, 0

            x, y, r = user_input[0], user_input[1:-1], user_input[-1]

            if x not in Game.letters or not y.isdigit() or int(y) not in range(1, Game.field_size + 1) or \
                    r not in ("H", "V"):
                self.message.append('Order not understood, data format error')
                return 0, 0, 0

            return Game.letters.index(x), int(y) - 1, 0 if r == 'H' else 1

        if input_type == "shot":

            if self.is_ai:
                if self.skill == 1:
                    x, y = choice(self.field.get_max_weight_cells())
                if self.skill == 0:
                    x, y = randrange(0, self.field.size), randrange(0, self.field.size)
            else:
                user_input = input().upper().replace(" ", "")
                x, y = user_input[0].upper(), user_input[1:]
                if x not in Game.letters or not y.isdigit() or int(y) not in range(1, Game.field_size + 1):
                    self.message.append('Order not understood, data format error')
                    return 500, 0
                x = Game.letters.index(x)
                y = int(y) - 1
            return x, y

    def make_shot(self, target_player):

        sx, sy = self.get_input('shot')
# shot result
        if sx + sy == 500 or self.field.radar[sx][sy] != Cell.empty_cell:
            return 'retry'

        shot_res = target_player.receive_shot((sx, sy))
# missed
        if shot_res == 'miss':
            self.field.radar[sx][sy] = Cell.miss_cell
# hit
        if shot_res == 'get':
            self.field.radar[sx][sy] = Cell.damaged_ship
# killed
        if type(shot_res) == Ship:
            destroyed_ship = shot_res
            self.field.mark_destroyed_ship(destroyed_ship, FieldPart.radar)
            self.enemy_ships.remove(destroyed_ship.size)
            shot_res = 'kill'

        self.field.recalculate_weight_map(self.enemy_ships)
# in case killed ship returns
        return shot_res

# the player will take a shot
    def receive_shot(self, shot):

        sx, sy = shot

        if type(self.field.map[sx][sy]) == Ship:
            ship = self.field.map[sx][sy]
            ship.hp -= 1

            if ship.hp <= 0:
                self.field.mark_destroyed_ship(ship, FieldPart.main)
                self.ships.remove(ship)
                return ship

            self.field.map[sx][sy] = Cell.damaged_ship
            return 'get'

        else:
            self.field.map[sx][sy] = Cell.miss_cell
            return 'miss'


class Ship:

    def __init__(self, size, x, y, rotation):

        self.size = size
        self.hp = size
        self.x = x
        self.y = y
        self.rotation = rotation
        self.set_rotation(rotation)

    def __str__(self):
        return Cell.ship_cell

    def set_position(self, x, y, r):
        self.x = x
        self.y = y
        self.set_rotation(r)

    def set_rotation(self, r):

        self.rotation = r

        if self.rotation == 0:
            self.width = self.size
            self.height = 1
        elif self.rotation == 1:
            self.width = 1
            self.height = self.size
        elif self.rotation == 2:
            self.y = self.y - self.size + 1
            self.width = self.size
            self.height = 1
        elif self.rotation == 3:
            self.x = self.x - self.size + 1
            self.width = 1
            self.height = self.size


if __name__ == '__main__':
    print("       Hello player!      ")
    print("This is a SEA BATTLE GAME ")
    print("    game input format:    ")
    print("     x - line number    ")
    print("    y - column number    ")
    print("   Let's start playing!   ")
    print("___________________________")
# make a list of two players and set their main parameters
    players = []
    players.append(Player(name=input('Enter player name:  '), is_ai=False, auto_ship=True, skill=1))
    players.append(Player(name='AI', is_ai=True, auto_ship=True, skill=1))

# create a game and run in an endless loop
    game = Game()

    while True:
# check the status and then act based on the status of the game
        game.status_check()

        if game.status == 'prepare':
            game.add_player(players.pop(0))

        if game.status == 'in game':
# in the main part of the game, clear the screen, add a message for the current player and draw the game
            Game.clear_screen()
            game.current_player.message.append("enter the coordinates for the shot: ")
            game.draw()
# clear the list of messages for the player. On the next turn, he will receive a new list of messages
            game.current_player.message.clear()
# the result of the shot based on the current player's shot at the next
            shot_result = game.current_player.make_shot(game.next_player)
# displaying a message to both the current player and the next # if you miss - pass the move to the next player
            if shot_result == 'miss':
                game.next_player.message.append(' {}, missed! '.format(game.current_player.name))
                game.next_player.message.append('your turn {}!'.format(game.next_player.name))
                game.switch_players()
                continue
            elif shot_result == 'retry':
                game.current_player.message.append(' TRY AGAIN !')
                continue
            elif shot_result == 'get':
                game.current_player.message.append('Great shot, keep shooting!')
                game.next_player.message.append('Our ship is damaged!')
                continue
            elif shot_result == 'kill':
                game.current_player.message.append('The enemy ship has been destroyed!')
                game.next_player.message.append('Bad news, our ship was destroyed... ')
                continue

        if game.status == 'game over':
            Game.clear_screen()
            game.next_player.field.draw_field(FieldPart.main)
            game.current_player.field.draw_field(FieldPart.main)
            print('It was the last ship {}'.format(game.next_player.name))
            print('{} won the match! Congratulations!'.format(game.current_player.name))
            break

    print('Thanks for the game!')
    input('')