def main_a(puzzle_input):
    lowest_location = 1e9
    almanac = puzzle_input.read().split('\n\n')
    seeds = list(map(int, almanac[0].split()[1:]))

    for seed in seeds:
        current_step_value = seed
        for current_map in almanac[1:]:
            next_step_value = current_step_value
            for map_range in current_map.splitlines()[1:]:
                dest_start, source_start, range_length = list(map(int, map_range.split()))
                if source_start <= current_step_value < source_start + range_length:
                    next_step_value = dest_start + current_step_value - source_start
            current_step_value = next_step_value

        if current_step_value < lowest_location:
            lowest_location = current_step_value
                

    return lowest_location


def main_b(puzzle_input):
    lowest_location = 1e9
    almanac = puzzle_input.read().split('\n\n')
    seeds = list(map(int, almanac[0].split()[1:]))

    list_of_conversions = []
    for current_map in almanac[1:]:
        mappings = {}
        for map_range in current_map.splitlines()[1:]:
            dest_start, source_start, range_length = list(map(int, map_range.split()))
            mappings[(source_start, source_start + range_length - 1)] = dest_start - source_start

        lowest_noted_range_start = min(mappings, key=lambda x: x[0])
        if lowest_noted_range_start[0] > 0:
            mappings[(0, lowest_noted_range_start[0] - 1)] = 0
        
        list_of_conversions.append({i: mappings[i] for i in sorted(mappings.keys(), key=lambda x: x[0])})

    for i in range(0, len(seeds), 2):
        seed_range = (seeds[i], seeds[i] + seeds[i+1] - 1)
        current_ranges = [seed_range]

        for mapping in list_of_conversions:
            range_starts, range_ends = [i[0] for i in current_ranges], [i[1] for i in current_ranges]
            map_starts, map_ends = [i[0] for i in mapping.keys()], [i[1] for i in mapping.keys()]
            breakpoints = sorted(set(range_starts + range_ends + map_starts + map_ends))
            
            ranges = []
            current_range_start = 0
            current_shift = 0
            range_active = False
            for b in breakpoints:
                if b in range_ends:
                    ranges.append((current_range_start + current_shift, b + current_shift))
                    range_active = False
                if b in range_starts:
                    current_range_start = b
                    range_active = True
                if b in map_starts:
                    if range_active and b != current_range_start:
                        ranges.append((current_range_start + current_shift, b + current_shift))
                        current_range_start = b + 1
                    current_shift = [v for k, v in mapping.items() if k[0] == b][0]
                if b in map_ends:
                    if range_active:
                        ranges.append((current_range_start + current_shift, b + current_shift))
                        current_range_start = b + 1
                    current_shift = 0
            current_ranges = ranges    

        lowest_range_start = min([i[0] for i in current_ranges])
        if lowest_range_start < lowest_location:
            lowest_location = lowest_range_start
    
    return lowest_location


if __name__ == '__main__':
    EXAMPLE_MODE = False
    file_name = 'example.txt' if EXAMPLE_MODE else 'input.txt'

    with open(file_name, 'r') as full_input:
        print(main_a(full_input))
        full_input.seek(0)
        print(main_b(full_input))