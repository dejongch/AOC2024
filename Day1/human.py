from util import get_input

input = get_input(1)

def part_one():
    left: list[int] = []
    right: list[int] = []

    for line in input:
        line_list = line.split(" ")
        left_item, right_item = line_list[0], line_list[-1]
        left.append(int(left_item))
        right.append(int(right_item))

    left.sort()
    right.sort()

    total = 0
    for index in range(len(left)):
        total += abs(left[index] - right[index])

    print(f"part one: {total}")


def part_two():
    left: list[int] = []
    right: dict[int, int] = {}

    for line in input:
        line_list = line.split(" ")
        left_item, right_item = int(line_list[0]), int(line_list[-1])
        left.append(left_item)
        right[right_item] = right.get(right_item, 0) + 1

    total = 0
    for left_item in left:
        total += left_item * right.get(left_item, 0)

    print(f"part two: {total}")

part_one()
part_two()