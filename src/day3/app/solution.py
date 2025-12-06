from shared.utils import read_input, parse_lines

# ===>>> Part 1 <<<===

def find_max_joltage(bank):
    max_joltage = 0

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            digit1 = bank[i]
            digit2 = bank[j]
            joltage = int(digit1 + digit2)

            if joltage > max_joltage:
                max_joltage = joltage
    
    return max_joltage

def solve_part_one(input_text):
    lines = parse_lines(input_text)
    total = 0

    for line in lines:
        max_joltage = find_max_joltage(line)
        total += max_joltage
    
    return total

# ===>>> Part 2 <<<===

def find_max_joltage_12(bank):
    digits_to_keep = 12
    digits_to_remove = len(bank) - digits_to_keep
    stack = []

    for digit in bank:
        while stack and digits_to_remove > 0 and stack[-1] < digit:
            stack.pop()
            digits_to_remove -= 1
        
        stack.append(digit)

    while digits_to_remove > 0:
        stack.pop()
        digits_to_remove -= 1
    
    result = int(''.join(stack[:digits_to_keep]))
    return result

def solve_part_two(input_text):
    lines = parse_lines(input_text)
    total = 0

    for bank in lines:
        max_joltage = find_max_joltage_12(bank)
        total += max_joltage
    
    return total

def main():
    input_text = read_input(day=3, part=1)
    result = solve_part_one(input_text)

    print(f"Part 1 - Total output joltage: {result}")

    result = solve_part_two(input_text)

    print(f"Part 2 - Total output joltage: {result}")

if __name__ == "__main__":
    main()