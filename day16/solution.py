def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def contains(required_details: dict[str, int], details: dict[str, int]) -> bool:
    for key, value in details.items():
        if key not in required_details:
            return False

        if required_details[key] != value:
            return False

    return True

def part1(filename: str) -> None:
    lines = get_lines(filename)

    aunt_dict_dict = {}
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")

        aunt_dict = {}
        id = int(split[:2][1][:-1])
        details = "".join(split[2:]).split(",")
        for detail in details:
            key, value = detail.split(":")
            aunt_dict[key] = int(value)
        aunt_dict_dict[id] = aunt_dict

    required_details = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    res = 0
    for aunt_id, aunt_dict in aunt_dict_dict.items():
        if contains(required_details, aunt_dict):
            if res > 0:
                raise ValueError("Multiple aunts found")
            res = aunt_id

    print("Solution Part 1: ", res)

def contains_2(required_details: dict[str, int], details: dict[str, int]) -> bool:
    for key, value in details.items():
        if key not in required_details:
            raise ValueError("Unknown key")

        if key == "cats" or key == "trees":
            if required_details[key] >= value:
                return False
        elif key == "pomeranians" or key == "goldfish":
            if required_details[key] <= value:
                return False
        else:
            if required_details[key] != value:
                return False

    return True

def part2(filename: str) -> None:
    lines = get_lines(filename)

    aunt_dict_dict = {}
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")

        aunt_dict = {}
        id = int(split[:2][1][:-1])
        details = "".join(split[2:]).split(",")
        for detail in details:
            key, value = detail.split(":")
            aunt_dict[key] = int(value)
        aunt_dict_dict[id] = aunt_dict

    required_details = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    res = 0
    for aunt_id, aunt_dict in aunt_dict_dict.items():
        if contains_2(required_details, aunt_dict):
            if res > 0:
                raise ValueError("Multiple aunts found")
            res = aunt_id

    print("Solution Part 2: ", res)

if __name__ == "__main__":
    part1("input1")
    part2("input1")

