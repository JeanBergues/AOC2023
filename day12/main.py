from functools import cache

def main_a(puzzle_input):
    total = 0

    for line in puzzle_input:
        record, conditions_str = line.split(' ')
        conditions = tuple(map(int, conditions_str.split(',')))

        total += count_possible(record, conditions)

    return total

@cache
def count_possible(record, conds):
    # Are the parameters empty? Then we are done
    if len(record) == 0 and len(conds) == 0:
        return 1
    
    # If there are still leftover conditions, this branch is not valid
    if len(record) == 0 and len(conds) > 0:
        return 0
    
    # If there are no more conditions but there is a broken pipe left, this branch is invalid
    if len(record) > 0 and len(conds) == 0 and '#' in record:
        return 0
    
    # There must still be sufficient room for all broken pipes: validity check comes later
    needed_room = sum(conds) + len(conds) - 1
    if needed_room > len(record):
        return 0

    # Started at working pipe, continue further
    if record[0] == '.': return count_possible(record[1:], conds)

    # Started at broken pipe: skip ahead if possible
    if record[0] == '#':
        # There must be room for the pipe, and it must not continue further
        if not '.' in record[0:conds[0]] and (conds[0] == len(record) or record[conds[0]] != '#'):
            return count_possible(record[(conds[0] + 1):], conds[1:])
        else:
            return 0

    # We are at a ? and it could be either broken or not: test both branches
    return count_possible('#' + record[1:], conds) + count_possible('.' + record[1:], conds)


def main_b(puzzle_input):
    total = 0

    for line in puzzle_input:
        record, conditions_str = line.split(' ')
        conditions = tuple(map(int, conditions_str.split(',')))
        unfolded_record = record

        for i in range(4):
            unfolded_record += '?' + record

        total += count_possible(unfolded_record, conditions * 5)

    return total


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))

"""
if n_unknown == n_damaged - n_known_damaged:
            total += 1
            continue

        # Make a pass with deductions
        rarr = list(record)
        c_cond = 0
        prev_d = 0
        for i in range(len(record)):
            if rarr[i] == '.':
                prev_d = 0
            elif rarr[i] == '#':
                prev_d += 1
                if prev_d == conditions[c_cond]:
                    c_cond += 1
                    if i < len(rarr) - 1: rarr[i+1] = '.'
            else:
                if i + conditions[c_cond] == len(rarr):
                    for j in range(i, len(rarr)):
                        rarr[j] = '#'
                elif rarr[i+conditions[c_cond]] == '#':
                    rarr[i] = '.'
        print(rarr)
"""