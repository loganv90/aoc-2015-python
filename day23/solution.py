def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def execute_instruction(instruction: str, state: dict[str, int]) -> None:
    parts = instruction.split(" ")
    if len(parts) < 2:
        raise ValueError("Invalid instruction")

    if parts[0] == "hlf":
        state[parts[1]] = state[parts[1]] // 2
        state["l"] += 1
    elif parts[0] == "tpl":
        state[parts[1]] = state[parts[1]] * 3
        state["l"] += 1
    elif parts[0] == "inc":
        state[parts[1]] += 1
        state["l"] += 1
    elif parts[0] == "jmp":
        state["l"] += int(parts[1])
    elif parts[0] == "jie":
        if state[parts[1].replace(",", "")] % 2 == 0:
            state["l"] += int(parts[2])
        else:
            state["l"] += 1
    elif parts[0] == "jio":
        if state[parts[1].replace(",", "")] == 1:
            state["l"] += int(parts[2])
        else:
            state["l"] += 1

def part1(filename: str) -> None:
    lines = get_lines(filename)

    instructions = []
    for line in lines:
        if len(line) <= 0:
            continue

        instructions.append(line)

    state = {
        "a": 0,
        "b": 0,
        "l": 0,
    }

    while state["l"] >= 0 and state["l"] < len(instructions):
        instruction = instructions[state["l"]]
        execute_instruction(instruction, state)

    print("Solution Part 1: ", state["b"])

def part2(filename: str) -> None:
    lines = get_lines(filename)

    instructions = []
    for line in lines:
        if len(line) <= 0:
            continue

        instructions.append(line)

    state = {
        "a": 1,
        "b": 0,
        "l": 0,
    }

    while state["l"] >= 0 and state["l"] < len(instructions):
        instruction = instructions[state["l"]]
        execute_instruction(instruction, state)

    print("Solution Part 2: ", state["b"])

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("input1")

