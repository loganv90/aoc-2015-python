def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def one_round(line: str) -> str:
    res = ""
    index = 0
    while index < len(line):
        char = line[index]

        length = 1
        while index + 1 < len(line) and char == line[index + 1]:
            index += 1
            length += 1
        res += str(length) + char

        index += 1

    return res

def part1(filename: str) -> None:
    lines = get_lines(filename)

    for line in lines:
        if len(line) <= 0:
            continue

        res_1 = one_round(line)
        res_40 = line
        for _ in range(40):
            res_40 = one_round(res_40)

        print("Solution Part 1: ", res_1, len(res_40))

def part2(filename: str) -> None:
    lines = get_lines(filename)

    for line in lines:
        if len(line) <= 0:
            continue

        res_1 = one_round(line)
        res_50 = line
        for _ in range(50):
            res_50 = one_round(res_50)

        print("Solution Part 2: ", res_1, len(res_50))

if __name__ == "__main__":
    part1("input1")
    part2("input1")

