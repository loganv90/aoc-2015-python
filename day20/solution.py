def calculate_presents(house: int) -> int:
    divisor_sum = 0
    for i in range(1, int(house ** 0.5) + 1):
        if house % i == 0:
            divisor_sum += i
            if i != house // i:
                divisor_sum += house // i
    return divisor_sum * 10

def calculate_presents_2(house: int) -> int:
    divisor_sum = 0
    for i in range(1, int(house ** 0.5) + 1):
        if house % i == 0:
            if house // (i) <= 50:
                divisor_sum += i
            if house // (house // i) <= 50:
                divisor_sum += house // i
    return divisor_sum * 11

def part1(present_limit: int) -> None:
    res = -1
    for i in range(1, present_limit // 10 + 1):
        presents = calculate_presents(i)
        if presents >= present_limit:
            res = i
            break

    print("Solution Part 1: ", res)

def part2(present_limit: int) -> None:
    res = -1
    for i in range(1, present_limit // 10 + 1):
        presents = calculate_presents_2(i)
        if presents >= present_limit:
            res = i
            break

    print("Solution Part 2: ", res)

if __name__ == "__main__":
    part1(150)
    part1(33100000)
    part2(150)
    part2(33100000)

