import itertools
import math

def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def get_qe(packages: tuple[int, ...]) -> int:
    qe = 1
    for package in packages:
        qe *= package
    return qe

def get_qe_of_smallest_group_with_lowest_qe(packages: list[int], weight: int) -> int:
    lowest_qe = math.inf
    lowest_l = math.inf

    for i in range(1, len(packages)):
        for combination in itertools.combinations(packages, i):
            s = sum(combination)
            if s != weight:
                continue

            l = len(combination)
            if l > lowest_l:
                continue

            qe = get_qe(combination)
            if qe < lowest_qe:
                lowest_qe = qe
                lowest_l = l

    if isinstance(lowest_qe, int):
        return lowest_qe
    raise ValueError("No solution found")

def part1(filename: str) -> None:
    lines = get_lines(filename)

    packages = []
    for line in lines:
        if len(line) <= 0:
            continue

        packages.append(int(line))

    weight = sum(packages) // 3
    qe = get_qe_of_smallest_group_with_lowest_qe(packages, weight)

    print("Solution Part 1: ", qe)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    packages = []
    for line in lines:
        if len(line) <= 0:
            continue

        packages.append(int(line))

    weight = sum(packages) // 4
    qe = get_qe_of_smallest_group_with_lowest_qe(packages, weight)

    print("Solution Part 2: ", qe)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

