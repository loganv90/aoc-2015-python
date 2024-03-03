from collections import deque

def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def find_wants(equation: str) -> list[str]:
    equation_split = equation.split(" ")

    if len(equation_split) == 1:
        if equation_split[0].isdigit():
            return []
        else:
            return [equation_split[0]]
    if len(equation_split) == 2:
        if equation_split[0] == "NOT":
            if equation_split[1].isdigit():
                return []
            else:
                return [equation_split[1]]
        else:
            raise ValueError("not expecting this")
    if len(equation_split) == 3:
        if equation_split[1] == "AND" or equation_split[1] == "OR":
            if equation_split[0].isdigit() and equation_split[2].isdigit():
                return []
            elif equation_split[0].isdigit():
                return [equation_split[2]]
            elif equation_split[2].isdigit():
                return [equation_split[0]]
            else:
                return [equation_split[0], equation_split[2]]
        elif equation_split[1] == "LSHIFT" or equation_split[1] == "RSHIFT":
            if equation_split[0].isdigit() and equation_split[2].isdigit():
                return []
            elif equation_split[0].isdigit():
                return [equation_split[2]]
            elif equation_split[2].isdigit():
                return [equation_split[0]]
            else:
                return [equation_split[0], equation_split[2]]
        else:
            raise ValueError("not expecting this")

    raise ValueError("not expecting this")

def evaluate(equation: str, values: dict) -> int:
    equation_split = equation.split(" ")

    if len(equation_split) == 1:
        if equation_split[0].isdigit():
            return int(equation_split[0])
        else:
            return values[equation_split[0]]
    if len(equation_split) == 2:
        if equation_split[0] == "NOT":
            if equation_split[1].isdigit():
                return int(equation_split[1]) ^ 0xFFFF
            else:
                return values[equation_split[1]] ^ 0xFFFF
        else:
            raise ValueError("not expecting this")
    if len(equation_split) == 3:
        if equation_split[1] == "AND":
            if equation_split[0].isdigit() and equation_split[2].isdigit():
                return int(equation_split[0]) & int(equation_split[2])
            elif equation_split[0].isdigit():
                return int(equation_split[0]) & values[equation_split[2]]
            elif equation_split[2].isdigit():
                return values[equation_split[0]] & int(equation_split[2])
            else:
                return values[equation_split[0]] & values[equation_split[2]]
        elif equation_split[1] == "OR":
            if equation_split[0].isdigit() and equation_split[2].isdigit():
                return int(equation_split[0]) | int(equation_split[2])
            elif equation_split[0].isdigit():
                return int(equation_split[0]) | values[equation_split[2]]
            elif equation_split[2].isdigit():
                return values[equation_split[0]] | int(equation_split[2])
            else:
                return values[equation_split[0]] | values[equation_split[2]]
        elif equation_split[1] == "LSHIFT":
            if equation_split[0].isdigit() and equation_split[2].isdigit():
                return int(equation_split[0]) << int(equation_split[2])
            elif equation_split[0].isdigit():
                return int(equation_split[0]) << values[equation_split[2]]
            elif equation_split[2].isdigit():
                return values[equation_split[0]] << int(equation_split[2])
            else:
                return values[equation_split[0]] << values[equation_split[2]]
        elif equation_split[1] == "RSHIFT":
            if equation_split[0].isdigit() and equation_split[2].isdigit():
                return int(equation_split[0]) >> int(equation_split[2])
            elif equation_split[0].isdigit():
                return int(equation_split[0]) >> values[equation_split[2]]
            elif equation_split[2].isdigit():
                return values[equation_split[0]] >> int(equation_split[2])
            else:
                return values[equation_split[0]] >> values[equation_split[2]]
        else:
            raise ValueError("not expecting this")

    raise ValueError("not expecting this")

def get_values(lines: list[str]) -> dict:
    queue = deque()
    want_to_wanter = dict()
    wanter_to_want = dict()
    values = dict()

    for line in lines:
        if len(line) <= 0:
            continue

        line = line.strip()
        line_split = line.split("->")
        value = line_split[0].strip()
        wanter = line_split[1].strip()

        values[wanter] = value

        wants = find_wants(value)
        for want in wants:
            if want not in want_to_wanter:
                want_to_wanter[want] = []
            want_to_wanter[want].append(wanter)
        wanter_to_want[wanter] = wants

    for wanter in wanter_to_want:
        if len(wanter_to_want[wanter]) <= 0:
            value = evaluate(values[wanter], values)
            values[wanter] = value
            queue.append(wanter)

    while len(queue) > 0:
        want = queue.popleft()
        if want not in want_to_wanter:
            continue

        for wanter in want_to_wanter[want]:
            wants = wanter_to_want[wanter]
            wants.remove(want)

            if len(wants) > 0:
                continue

            value = evaluate(values[wanter], values)
            values[wanter] = value
            queue.append(wanter)
    
    return values

def part1(filename: str) -> None:
    lines = get_lines(filename)
    values = get_values(lines)

    if 'a' in values:
        print("Solution Part 1: ", values['a'])
    else:
        print("Solution Part 1: ", values)

def part2(filename: str) -> None:
    lines = get_lines(filename)
    values = get_values(lines)

    signal_a = values["a"]
    queue = deque()
    want_to_wanter = dict()
    wanter_to_want = dict()
    values = dict()

    for line in lines:
        if len(line) <= 0:
            continue

        line = line.strip()
        line_split = line.split("->")
        value = line_split[0].strip()
        wanter = line_split[1].strip()

        values[wanter] = value

        wants = find_wants(value)
        for want in wants:
            if want not in want_to_wanter:
                want_to_wanter[want] = []
            want_to_wanter[want].append(wanter)

        if wanter == "b":
            continue
        wanter_to_want[wanter] = wants

    for wanter in wanter_to_want:
        if len(wanter_to_want[wanter]) <= 0:
            value = evaluate(values[wanter], values)
            values[wanter] = value
            queue.append(wanter)

    queue.append("b")
    values["b"] = signal_a

    while len(queue) > 0:
        want = queue.popleft()
        if want not in want_to_wanter:
            continue

        for wanter in want_to_wanter[want]:
            wants = wanter_to_want[wanter]
            wants.remove(want)

            if len(wants) > 0:
                continue

            value = evaluate(values[wanter], values)
            values[wanter] = value
            queue.append(wanter)

    if 'a' in values:
        print("Solution Part 2: ", values['a'])
    else:
        print("Solution Part 2: ", values)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("input1")

