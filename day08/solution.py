def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def find_parsed_length(line: str) -> int:
    res = len(line) - 2

    i = 0
    while i < len(line)-1:
        if line[i] == "\\" and line[i+1] == "x":
            res -= 3
        elif line[i] == "\\":
            res -= 1
            i += 1

        i += 1

    return res

def find_encoded_length(line: str) -> int:
    res = len(line) + 2

    i = 0
    while i < len(line):
        if line[i] == "\\" or line[i] == "\"":
            res += 1

        i += 1

    return res

def part1(filename: str) -> None:
    lines = get_lines(filename)

    res = 0
    for line in lines:
        if len(line) <= 0:
            continue

        original_length = len(line)
        parsed_length = find_parsed_length(line)
        res += original_length - parsed_length

    print("Solution Part 1: ", res)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    res = 0
    for line in lines:
        if len(line) <= 0:
            continue

        original_length = len(line)
        encoded_length = find_encoded_length(line)
        res += encoded_length - original_length

    print("Solution Part 2: ", res)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

