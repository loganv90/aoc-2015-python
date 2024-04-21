import math

def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def get_permutations(arr: list[str]) -> list[list[str]]:
    if len(arr) == 1:
        return [arr]

    res = []
    for i in range(len(arr)):
        sub_arr = arr[:i] + arr[i+1:]
        sub_permutations = get_permutations(sub_arr)
        for sub_perm in sub_permutations:
            res.append([arr[i]] + sub_perm)

    return res

def part1(filename: str) -> None:
    lines = get_lines(filename)

    cities = set()
    distances = dict()
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        from_city = split[0]
        to_city = split[2]
        distance = int(split[4])

        cities.add(from_city)
        cities.add(to_city)

        if from_city not in distances:
            distances[from_city] = dict()
        if to_city not in distances:
            distances[to_city] = dict()

        distances[from_city][to_city] = distance
        distances[to_city][from_city] = distance

    permutations = get_permutations(list(cities))

    g_res = math.inf
    for perm in permutations:
        l_res = 0
        for i in range(len(perm)-1):
            l_res += distances[perm[i]][perm[i+1]]
        g_res = min(g_res, l_res)

    print("Solution Part 1: ", g_res)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    cities = set()
    distances = dict()
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        from_city = split[0]
        to_city = split[2]
        distance = int(split[4])

        cities.add(from_city)
        cities.add(to_city)

        if from_city not in distances:
            distances[from_city] = dict()
        if to_city not in distances:
            distances[to_city] = dict()

        distances[from_city][to_city] = distance
        distances[to_city][from_city] = distance

    permutations = get_permutations(list(cities))

    g_res = 0
    for perm in permutations:
        l_res = 0
        for i in range(len(perm)-1):
            l_res += distances[perm[i]][perm[i+1]]
        g_res = max(g_res, l_res)

    print("Solution Part 2: ", g_res)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

