def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)

    total = 0
    for line in lines:
        if line == "":
            continue

        split = line.split("x")
        length = int(split[0])
        width = int(split[1])
        height = int(split[2])

        lw = length * width
        wh = width * height
        hl = height * length

        smallest = min(lw, wh, hl)
        total += 2 * length * width + 2 * width * height + 2 * height * length + smallest

    print("Solution Part 1: ", total)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    total = 0
    for line in lines:
        if line == "":
            continue

        split = line.split("x")
        length = int(split[0])
        width = int(split[1])
        height = int(split[2])

        lw = 2 * length + 2 * width
        wh = 2 * width + 2 * height
        hl = 2 * height + 2 * length

        smallest = min(lw, wh, hl)
        total += length * width * height + smallest

    print("Solution Part 1: ", total)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

