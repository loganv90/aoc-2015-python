def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def increment(password: list[str]) -> list[str]:
    index = len(password) - 1

    new_ord = ord(password[index]) + 1
    if new_ord > ord("z"):
        new_ord = ord("a")
        carry = True
    else:
        carry = False
    password[index] = chr(new_ord)

    while carry and index >= 0:
        index -= 1

        new_ord = ord(password[index]) + 1
        if new_ord > ord("z"):
            new_ord = ord("a")
            carry = True
        else:
            carry = False
        password[index] = chr(new_ord)

    return password

def check(password: list[str]) -> bool:
    for i in password:
        if i == "i" or i == "o" or i == "l":
            return False

    index = 0
    success = 0
    while index <= len(password) - 2:
        if ord(password[index]) == ord(password[index + 1]):
            success += 1
            index += 2
        else:
            index += 1
    if success < 2:
        return False

    success = False
    for i in range(len(password) - 3):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i]) + 2 == ord(password[i + 2]):
            success = True
            break
    return success

def part1(filename: str) -> None:
    lines = get_lines(filename)

    for line in lines:
        if len(line) <= 0:
            continue

        password = list(line)
        password = increment(password)
        while not check(password):
            password = increment(password)

        print("Solution Part 1: ", password)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    for line in lines:
        if len(line) <= 0:
            continue

        password = list(line)
        password = increment(password)
        while not check(password):
            password = increment(password)
        password = increment(password)
        while not check(password):
            password = increment(password)

        print("Solution Part 2: ", password)

if __name__ == "__main__":
    part1("input1")
    part2("input1")

