def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def count_combinations(sizes: list[int], cap: int) -> int:
    if cap == 0:
        return 1

    count = 0
    for i in range(0, len(sizes)):
        inc = sizes[i]
        sub = sizes[i+1:]
        count += count_combinations(sub, cap - inc)

    return count

def part1(filename: str, cap: int) -> None:
    lines = get_lines(filename)

    sizes = []
    for line in lines:
        if len(line) <= 0:
            continue
        number = int(line)
        sizes.append(number)
    sizes.sort()

    count = count_combinations(sizes, cap)
    
    print("Solution Part 1: ", count)

def count_combinations_2(sizes: list[int], space_left: int, containers_used: int) -> list[tuple[int, int]]:
    if space_left == 0:
        return [(1, containers_used)]

    count = []
    for i in range(0, len(sizes)):
        inc = sizes[i]
        sub = sizes[i+1:]
        count.extend(count_combinations_2(sub, space_left - inc, containers_used + 1))

    return count

def part2(filename: str, cap: int) -> None:
    lines = get_lines(filename)

    sizes = []
    for line in lines:
        if len(line) <= 0:
            continue
        number = int(line)
        sizes.append(number)
    sizes.sort()

    stats = count_combinations_2(sizes, cap, 0)

    min_containers = 1000000
    count = 0
    for stat in stats:
        _, containers = stat
        if containers < min_containers:
            min_containers = containers
            count = 1
        elif containers == min_containers:
            count += 1
    
    print("Solution Part 2: ", count)

if __name__ == "__main__":
    part1("test1", 25)
    part1("input1", 150)
    part2("test1", 25)
    part2("input1", 150)

