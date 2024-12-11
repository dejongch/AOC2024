from util import get_input

input = get_input(2)

def check_step_safe(current, next, increasing):
    diff = current - next
    if increasing is None:
        increasing = diff < 0
    return (increasing, not (
        diff == 0
        or (increasing and diff > 0) 
        or (not increasing and diff < 0)
        or abs(diff) > 3
    ))

def check_steps_safe(steps, increasing = None, allow_skip=False):
    safe = True
    index = 0
    while index < (len(steps) - 1):
        current = int(steps[index])
        next = int(steps[index + 1])
        increasing, safe = check_step_safe(current, next, increasing)

        if not safe:
            if allow_skip:
                allow_skip = False
                if index < len(steps) - 2:
                    increasing, safe = check_step_safe(current, int(steps[index + 2]), increasing)
                else:
                    safe = True
                index += 1
        if not safe:
            break
        index += 1
    return (safe, increasing)
        



def part_one():
    num_safe = 0
    for report in input:
        if check_steps_safe(report.split(" "))[0]:
            num_safe += 1
    print(f"part one: {num_safe}")

def part_two():
    num_safe = 0
    for report in input:
        steps = report.split(" ")
        safe, increasing = check_steps_safe(steps[:4])
        allow_skip = True
        if not safe:
            skip_index = 0
            allow_skip = False
            while skip_index < 3 and not safe:
                safe, increasing = check_steps_safe(steps[:skip_index] + steps[skip_index+1:4])
                skip_index += 1
        if safe:
            if check_steps_safe(steps[3:], increasing, allow_skip)[0]:
                num_safe += 1

    print(f"part two: {num_safe}")

part_one()
part_two()