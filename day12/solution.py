import json

def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def count_numbers(data) -> int:
    if type(data) == int:
        return data
    if type(data) == str:
        return 0
    if type(data) == list:
        return sum([count_numbers(d) for d in data])
    if type(data) == dict:
        return sum([count_numbers(data[key]) for key in data])
    raise ValueError(f"Unknown type {type(data)}")

def part1(filename: str) -> None:
    lines = get_lines(filename)

    for line in lines:
        if len(line) <= 0:
            continue

        data = json.loads(line)
        count = count_numbers(data)

        print("Solution Part 1: ", count)

def count_numbers_2(data) -> int:
    if type(data) == int:
        return data
    if type(data) == str:
        return 0
    if type(data) == list:
        return sum([count_numbers_2(d) for d in data])
    if type(data) == dict:
        if "red" in data.values():
            return 0
        return sum([count_numbers_2(data[key]) for key in data])
    raise ValueError(f"Unknown type {type(data)}")

def part2(filename: str) -> None:
    lines = get_lines(filename)

    for line in lines:
        if len(line) <= 0:
            continue

        data = json.loads(line)
        count = count_numbers_2(data)

        print("Solution Part 2: ", count)

if __name__ == "__main__":
    part1("test1")
    part1("test2")
    part1("test3")
    part1("test4")
    part1("test5")
    part1("test6")
    part1("test7")
    part1("test8")
    part1("input1")
    part2("test1")
    part2("test9")
    part2("test10")
    part2("test11")
    part2("input1")

