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

    map = {}
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        if len(split) != 11:
            raise ValueError("Invalid line")

        name1 = split[0]
        sign = 1 if split[2] == "gain" else -1
        value = int(split[3])
        name2 = split[10][:-1]

        if name1 not in map:
            map[name1] = {}
        map[name1][name2] = sign * value

    people = list(map.keys())
    permutations = get_permutations(people)

    g_happiness = 0
    for perm in permutations:
        l_happiness = 0
        for i in range(len(perm)):
            left = i - 1 if i > 0 else len(perm)-1
            right = i + 1 if i < len(perm)-1 else 0
            l_happiness += map[perm[i]][perm[left]]
            l_happiness += map[perm[i]][perm[right]]

        if l_happiness > g_happiness:
            g_happiness = l_happiness

    print("Solution Part 1: ", g_happiness)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    map = {}
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        if len(split) != 11:
            raise ValueError("Invalid line")

        name1 = split[0]
        sign = 1 if split[2] == "gain" else -1
        value = int(split[3])
        name2 = split[10][:-1]

        if name1 not in map:
            map[name1] = {}
        map[name1][name2] = sign * value

    people = list(map.keys()) + ["Me"]
    permutations = get_permutations(people)

    g_happiness = 0
    for perm in permutations:
        l_happiness = 0
        for i in range(len(perm)):
            left = i - 1 if i > 0 else len(perm)-1
            right = i + 1 if i < len(perm)-1 else 0

            l_map = map.get(perm[i], {})
            l_happiness += l_map.get(perm[left], 0)

            r_map = map.get(perm[i], {})
            l_happiness += r_map.get(perm[right], 0)

        if l_happiness > g_happiness:
            g_happiness = l_happiness

    print("Solution Part 2: ", g_happiness)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

