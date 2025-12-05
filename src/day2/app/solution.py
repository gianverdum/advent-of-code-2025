from shared.utils import read_input

# ===>>> Part one <<<===

def parse_ranges(input_text):
    cleaned = input_text.strip().replace('\n', '')
    range_strings = cleaned.split(',')

    ranges = []
    for range_str in range_strings:
        parts = range_str.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start,end))
    
    return ranges

def is_invalid_id(num):
    num_str = str(num)

    if len(num_str) % 2 != 0:
        return False
    
    middle_index = len(num_str) // 2
    first_half = num_str[:middle_index]
    second_half = num_str[middle_index:]

    return first_half == second_half

def solve_part_one(input_text):
    ranges = parse_ranges(input_text)
    total_sum = 0

    for start, end in ranges:
        for num in range(start, end +1):
            if is_invalid_id(num):
                total_sum += num
    
    return total_sum

# ===>>> Part two <<<===

def is_invalid_id_part2(num):
    num_str = str(num)
    length = len(num_str)

    for pattern_size in range(1, length):
        if length % pattern_size == 0:
            repetitions = length // pattern_size
            if repetitions >= 2:
                pattern = num_str[:pattern_size]
                if pattern * repetitions == num_str:
                    return True
    
    return False

def solve_part_two(input_text):
    ranges = parse_ranges(input_text)
    total_sum = 0

    for start, end in ranges:
        for num in range(start, end +1):
            if is_invalid_id_part2(num):
                total_sum += num
    
    return total_sum

def main():
    input_text = read_input(day=2, part=1)
    result = solve_part_one(input_text)

    print(f"Part 1 - Sum of invalid IDs: {result}")

    result = solve_part_two(input_text)

    print(f"Part 2 - Sum of invalid IDs: {result}")

if __name__ == "__main__":
    main()