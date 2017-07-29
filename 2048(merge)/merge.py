"""
Merge function for 2048 game.
"""


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
