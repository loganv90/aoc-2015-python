def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)

    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        if len(line) <= 0:
            continue

        line = line.strip()
        line = line.replace(",", " ")
        line_split = line.split(" ")
        if len(line_split) != 6 and len(line_split) != 7:
            raise ValueError("not expecting this")
        if len(line_split) == 7:
            line_split = line_split[1:]

        command = line_split[0]
        start_row = int(line_split[1])
        start_col = int(line_split[2])
        end_row = int(line_split[4])
        end_col = int(line_split[5])

        if command == "toggle":
            func = lambda x: not x
        elif command == "on":
            func = lambda _: True
        elif command == "off":
            func = lambda _: False
        else:
            raise ValueError("not expecting this")

        for r in range(start_row, end_row+1):
            for c in range(start_col, end_col+1):
                lights[r][c] = func(lights[r][c])

    count = 0
    for r in range(1000):
        for c in range(1000):
            if lights[r][c]:
                count += 1

    print("Solution Part 1: ", count)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        if len(line) <= 0:
            continue

        line = line.strip()
        line = line.replace(",", " ")
        line_split = line.split(" ")
        if len(line_split) != 6 and len(line_split) != 7:
            raise ValueError("not expecting this")
        if len(line_split) == 7:
            line_split = line_split[1:]

        command = line_split[0]
        start_row = int(line_split[1])
        start_col = int(line_split[2])
        end_row = int(line_split[4])
        end_col = int(line_split[5])

        if command == "toggle":
            func = lambda x: x + 2
        elif command == "on":
            func = lambda x: x + 1
        elif command == "off":
            func = lambda x: max(0, x-1)
        else:
            raise ValueError("not expecting this")

        for r in range(start_row, end_row+1):
            for c in range(start_col, end_col+1):
                lights[r][c] = func(lights[r][c])

    count = 0
    for r in range(1000):
        for c in range(1000):
            count += lights[r][c]

    print("Solution Part 2: ", count)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

