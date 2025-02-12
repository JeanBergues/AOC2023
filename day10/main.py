def main_a(puzzle_input):
    total = 0

    symbol_dirs = {
        '|': [(0, -1), (0, 1)],
        '-': [(-1, 0), (1, 0)],
        'L': [(0, -1), (1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, 1), (-1, 0)],
        'F': [(0, 1), (1, 0)],
    }

    pipes_map = list(puzzle_input.read().splitlines())
    X_BOUND, Y_BOUND = len(pipes_map[0]), len(pipes_map)

    # Find starting position
    start_pos = (0, 0)
    for x in range(X_BOUND):
        for y in range(Y_BOUND):
            if pipes_map[y][x] == 'S':
                start_pos = (x, y)
                break
    
    # Search for the loop
    for start_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        loop_length = 1
        current_pos = start_pos
        current_dir = start_dir
        reached_start = False

        while not reached_start:
            next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])

            # Check if next position is the starting position
            if next_pos == start_pos:
                reached_start = True
                break
            
            # Check if pipe can be entered from current coordinate
            if (current_dir[0] * -1, current_dir[1] * -1) not in symbol_dirs[pipes_map[next_pos[1]][next_pos[0]]]:
                break

            loop_length += 1
            current_dir = [d for d in symbol_dirs[pipes_map[next_pos[1]][next_pos[0]]] if d != (current_dir[0] * -1, current_dir[1] * -1)][0]
            current_pos = next_pos

        if reached_start:
            return loop_length // 2

    return total


def is_in_loop(pos, loop_coords, pipes_map, X_BOUND, Y_BOUND):
    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ignore = '|' if d[0] == 0 else '-'
        reached_edge = False
        cpos = pos
        n_loop_pipes = 0
        while not reached_edge:
            npos = (cpos[0] + d[0], cpos[1] + d[1])
            if 0 <= cpos[0] < X_BOUND and 0 <= cpos[1] < Y_BOUND:
                n_loop_pipes += 1 if npos in loop_coords and pipes_map[npos[1]][npos[0]] != ignore else 0
                cpos = npos
            else:
                reached_edge = True
        if n_loop_pipes % 2 == 1:
            return True
        if n_loop_pipes == 0:
            return False
        
    return False


def main_b(puzzle_input):
    total = 0

    symbol_dirs = {
        '|': [(0, -1), (0, 1)],
        '-': [(-1, 0), (1, 0)],
        'L': [(0, -1), (1, 0)],
        'J': [(0, -1), (-1, 0)],
        '7': [(0, 1), (-1, 0)],
        'F': [(0, 1), (1, 0)],
    }

    pipes_map = list(puzzle_input.read().splitlines())
    X_BOUND, Y_BOUND = len(pipes_map[0]), len(pipes_map)

    # Find starting position
    start_pos = (0, 0)
    for x in range(X_BOUND):
        for y in range(Y_BOUND):
            if pipes_map[y][x] == 'S':
                start_pos = (x, y)
                break
    
    loop_coords = set()
    # Search for the loop
    for start_dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        current_pos = start_pos
        current_dir = start_dir
        reached_start = False
        path_set = set([start_pos])

        while not reached_start:
            next_pos = (current_pos[0] + current_dir[0], current_pos[1] + current_dir[1])

            # Check if next position is the starting position
            if next_pos == start_pos:
                reached_start = True
                break
            
            # Check if pipe can be entered from current coordinate
            if (current_dir[0] * -1, current_dir[1] * -1) not in symbol_dirs[pipes_map[next_pos[1]][next_pos[0]]]:
                break

            path_set.add(next_pos)
            current_dir = [d for d in symbol_dirs[pipes_map[next_pos[1]][next_pos[0]]] if d != (current_dir[0] * -1, current_dir[1] * -1)][0]
            current_pos = next_pos

        if reached_start:
            loop_coords = path_set

    for x in range(X_BOUND):
        for y in range(Y_BOUND):
            if (x, y) in loop_coords:
                continue
            if is_in_loop((x, y), loop_coords, pipes_map, X_BOUND, Y_BOUND):
                total += 1

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.