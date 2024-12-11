from util import get_input
import re

input = "".join(get_input(3))
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def get_string_total(str):
    total = 0    
    matches = re.findall(pattern, str)
    for num1, num2 in matches:
        total += int(num1) * int(num2)
    return total

def part_one():
    return get_string_total(input)

def part_two():
    commands = input.split("don't()")

    total = get_string_total(commands[0])

    for commands_index in range(1, len(commands)):
        split_command = commands[commands_index].split("do()")
        for split_command_index in range(1, len(split_command)):
            total += get_string_total(split_command[split_command_index])

    return total


print(f"part one: {part_one()}")
print(f"part two: {part_two()}")