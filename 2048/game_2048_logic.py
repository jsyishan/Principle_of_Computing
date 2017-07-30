"""
Clone of 2048 game.
"""

# import poc_2048_gui

# Directions, DO NOT MODIFY
import random

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    len_of_line = len(line)
    target = []

    for _ in range(len_of_line):
        target.append(0)

    _index = 0 # the index of the target list
    for index in range(len_of_line):
        if line[index] != 0:
            if target[_index] == 0:
                target[_index] = line[index]
                # _index = _index + 1
            elif target[_index] == line[index]:
                target[_index] = line[index] * 2
                _index = _index + 1
            else:
                _index = _index + 1
                target[_index] = line[index]

    return target


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._game_kernel = {
            'height':  grid_height,
            'width': grid_width,
            'zone': [[]],
            'indices': {
                UP: [],
                DOWN: [],
                LEFT: [],
                RIGHT: []
            }
        }
        self.computing_indices()
        self.reset()

    def computing_indices(self):
        """
        Pre-computing a list of the indices for the initial
        tiles in all directions.
        """
        for col in range(self.get_grid_width()):
            self._game_kernel['indices'][UP].append((0, col))
            self._game_kernel['indices'][DOWN].append(((self.get_grid_height() - 1), col))
        for row in range(self.get_grid_height()):
            self._game_kernel['indices'][LEFT].append((row, 0))
            self._game_kernel['indices'][RIGHT].append((row, self.get_grid_width() - 1))

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._game_kernel['zone'] = [[
            0
            for _ in range(self.get_grid_width())]
            for _ in range(self.get_grid_height())
        ]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        grid = ""
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                grid = grid + str(self.get_tile(row, col)) + " "
            grid = grid + "\n"
        return grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._game_kernel['height']

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._game_kernel['width']

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        changed = False
        index = 0
        for grid in self._game_kernel['indices'][direction]:
            tile_values = []
            position = []
            if direction == UP or direction == DOWN:
                for pos in range(self.get_grid_height()):
                    position.append((grid[0] + pos * OFFSETS[direction][0], grid[1]))
                    # tile_values.append(self._game_kernel['zone'][position[pos][0]][position[pos][1]])
                    tile_values.append(self.get_tile(position[pos][0], position[pos][1]))
                # print position
                # print tile_values
                merged_values = merge(tile_values)
                # print merged_values
                for pos, row in zip(position, range(self.get_grid_height())):
                    # print self.get_tile(pos[0], pos[1])
                    if merged_values[pos[0]] != self.get_tile(row, index):
                        self.set_tile(row, index, merged_values[pos[0]])
                        changed = True
            else:
                for pos in range(self.get_grid_width()):
                    position.append((grid[0], grid[1] + pos * OFFSETS[direction][1]))
                    # tile_values.append(self._game_kernel['zone'][position[pos][0]][position[pos][1]])
                    tile_values.append(self.get_tile(position[pos][0], position[pos][1]))
                # print tile_values
                # print position
                merged_values = merge(tile_values)
                # print merged_values
                for pos, col in zip(position, range(self.get_grid_width())):
                    # print self.get_tile(pos[0], pos[1])
                    # print self.get_tile(row, index)
                    if merged_values[pos[1]] != self.get_tile(index, col):
                        self.set_tile(index, col, merged_values[pos[1]])
                        changed = True
            index = index + 1
            # print tile_values
        if changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        while True:
            rand_row = random.randint(0, self.get_grid_height() - 1)
            rand_col = random.randint(0, self.get_grid_width() - 1)
            if self._game_kernel['zone'][rand_row][rand_col] == 0:
                rand_pre_value = random.random()
                rand_value = 2
                if rand_pre_value > 0.9:
                    rand_value = 4
                self._game_kernel['zone'][rand_row][rand_col] = rand_value
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        try:
            self._game_kernel['zone'][row][col] = value
        except IndexError:
            print 'index of the grid(row or col) is out of range'

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        try:
            return self._game_kernel['zone'][row][col]
        except IndexError:
            print 'index of the grid(row or col) is out of range'

obj = TwentyFortyEight(4, 5)
obj.set_tile(0, 0, 8)
obj.set_tile(0, 1, 16)
obj.set_tile(0, 2, 8)
obj.set_tile(0, 3, 16)
obj.set_tile(0, 4, 8)
obj.set_tile(1, 0, 16)
obj.set_tile(1, 1, 8)
obj.set_tile(1, 2, 16)
obj.set_tile(1, 3, 8)
obj.set_tile(1, 4, 16)
obj.set_tile(2, 0, 8)
obj.set_tile(2, 1, 16)
obj.set_tile(2, 2, 8)
obj.set_tile(2, 3, 16)
obj.set_tile(2, 4, 8)
obj.set_tile(3, 0, 16)
obj.set_tile(3, 1, 8)
obj.set_tile(3, 2, 16)
obj.set_tile(3, 3, 8)
obj.set_tile(3, 4, 16)
print obj
obj.move(RIGHT)
# print "obj1 before\n", obj

# obj2 = TwentyFortyEight(4, 4) # this should be OK!
#
# obj.move(DOWN)
# print "obj1 after\n", obj
#
# print "obj2\n", obj2
# # # poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
