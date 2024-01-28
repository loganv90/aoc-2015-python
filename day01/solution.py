def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)

    floor = 0
    for line in lines:
        if line == "":
            continue

        for c in line:
            if c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
            else:
                raise Exception("Invalid character: " + c)

    print("Solution Part 1: ", floor)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    floor = 0
    for line in lines:
        if line == "":
            continue

        for i in range(len(line)):
            if line[i] == "(":
                floor += 1
            elif line[i] == ")":
                floor -= 1
            else:
                raise Exception("Invalid character: " + line[i])

            if floor < 0:
                print("Solution Part 2: ", i + 1)
                return

    raise Exception("Solution not found")

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test2")
    part2("input1")

