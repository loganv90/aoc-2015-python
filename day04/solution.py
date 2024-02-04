import hashlib

def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)
    line = lines[0]

    current = 0
    while True:
        if hashlib.md5(f"{line}{current}".encode()).hexdigest().startswith("00000"):
            break
        current += 1

    print("Solution Part 1: ", current)

def part2(filename: str) -> None:
    lines = get_lines(filename)
    line = lines[0]

    current = 0
    while True:
        if hashlib.md5(f"{line}{current}".encode()).hexdigest().startswith("000000"):
            break
        current += 1

    print("Solution Part 1: ", current)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("input1")

