from day2.app.solution import is_invalid_id, parse_ranges, solve_part_one, is_invalid_id_part2, solve_part_two

def test_is_invalid_id():
    assert is_invalid_id(11) == True
    assert is_invalid_id(22) == True
    assert is_invalid_id(99) == True
    assert is_invalid_id(1010) == True
    assert is_invalid_id(6464) == True
    assert is_invalid_id(123123) == True
    assert is_invalid_id(222222) == True
    
    assert is_invalid_id(12) == False
    assert is_invalid_id(101) == False
    assert is_invalid_id(111) == False
    assert is_invalid_id(123456) == False
    assert is_invalid_id(100) == False

def test_parse_ranges():
    input_text = "11-22,95-115,998-1012"
    ranges = parse_ranges(input_text)
    assert ranges == [(11,22), (95,115), (998,1012)]

    input_text = "11-22"
    ranges = parse_ranges(input_text)
    assert ranges == [(11,22)]

def test_example_from_puzzle():
    example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    
    result = solve_part_one(example_input)
    assert result == 1227775554

def test_is_invalid_id_part2():
    assert is_invalid_id_part2(11) == True
    assert is_invalid_id_part2(1010) == True
    assert is_invalid_id_part2(12341234) == True
    assert is_invalid_id_part2(111) == True
    assert is_invalid_id_part2(999) == True
    assert is_invalid_id_part2(123123123) == True
    assert is_invalid_id_part2(1212121212) == True
    assert is_invalid_id_part2(1111111) == True
    
    assert is_invalid_id_part2(12) == False
    assert is_invalid_id_part2(123456) == False
    assert is_invalid_id_part2(100) == False

def test_example_from_puzzle_part2():
    example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    
    result = solve_part_two(example_input)
    assert result == 4174379265