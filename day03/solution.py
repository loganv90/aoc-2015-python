def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)

    x = 0
    y = 0
    houses = {(int(x), int(y))}

    for line in lines:
        if line == "":
            continue

        for c in line:
            if c == "^":
                y += 1
            elif c == "v":
                y -= 1
            elif c == ">":
                x += 1
            elif c == "<":
                x -= 1
            houses.add((x, y))

    print("Solution Part 1: ", len(houses))

def part2(filename: str) -> None:
    lines = get_lines(filename)

    santas = [[0, 0], [0, 0]]
    houses = {(int(0), int(0))}

    for line in lines:
        if line == "":
            continue

        for i, c in enumerate(line):
            index = i % 2

            if c == "^":
                santas[index] = [santas[index][0], santas[index][1] + 1]
            elif c == "v":
                santas[index] = [santas[index][0], santas[index][1] - 1]
            elif c == ">":
                santas[index] = [santas[index][0] + 1, santas[index][1]]
            elif c == "<":
                santas[index] = [santas[index][0] - 1, santas[index][1]]

            houses.add((santas[index][0], santas[index][1]))

    print("Solution Part 2: ", len(houses))

if __name__ == "__main__":
    part1("test1")
    part1("test2")
    part1("input1")
    part2("test1")
    part2("test2")
    part2("input1")

