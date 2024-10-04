def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def multiply_ingredient(ingredient: tuple[str, int, int, int, int, int], cap: int) -> tuple[str, int, int, int, int, int]:
    name, capacity, durability, flavor, texture, calories = ingredient
    return name, capacity * cap, durability * cap, flavor * cap, texture * cap, calories * cap

def score_ingredients(chosen_ingredients: list[tuple[str, int, int, int, int, int]]) -> tuple[int, int]:
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for ingredient in chosen_ingredients:
        _, cap, dur, flav, text, cal = ingredient
        capacity += cap
        durability += dur
        flavor += flav
        texture += text
        calories += cal

    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        return 0, calories
    return capacity * durability * flavor * texture, calories

def get_best_score(ingredients: list[tuple[str, int, int, int, int, int]], cal_spec=False) -> int:
    best_score = 0
    cap = 100
    for i in range(0, cap+1):
        for j in range(0, cap+1-i):
            for k in range(0, cap+1-i-j):
                l = cap - i - j - k

                ingredient_0 = multiply_ingredient(ingredients[0], i)
                ingredient_1 = multiply_ingredient(ingredients[1], j)
                ingredient_2 = multiply_ingredient(ingredients[2], k)
                ingredient_3 = multiply_ingredient(ingredients[3], l)

                score, calories = score_ingredients([ingredient_0, ingredient_1, ingredient_2, ingredient_3])
                if cal_spec and calories != 500:
                    continue
                if score > best_score:
                    best_score = score
    return best_score

def part1(filename: str) -> None:
    lines = get_lines(filename)

    ingredient_list = []
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        if len(split) != 11:
            raise ValueError("Invalid line")

        name = split[0]
        capacity = int(split[2][:-1])
        durability = int(split[4][:-1])
        flavor = int(split[6][:-1])
        texture = int(split[8][:-1])
        calories = int(split[10])

        ingredient_list.append((name, capacity, durability, flavor, texture, calories))

    best_score = get_best_score(ingredient_list)

    print("Solution Part 1: ", best_score)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    ingredient_list = []
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        if len(split) != 11:
            raise ValueError("Invalid line")

        name = split[0]
        capacity = int(split[2][:-1])
        durability = int(split[4][:-1])
        flavor = int(split[6][:-1])
        texture = int(split[8][:-1])
        calories = int(split[10])

        ingredient_list.append((name, capacity, durability, flavor, texture, calories))

    best_score = get_best_score(ingredient_list, True)

    print("Solution Part 2: ", best_score)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test1")
    part2("input1")

