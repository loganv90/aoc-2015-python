def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)

    vowels = "aeiou"
    forbiddens = ["ab", "cd", "pq", "xy"]
    niceCount = 0
    for line in lines:
        if len(line) <= 0:
            continue

        vowelCount = 0
        doubleLetter = False
        forbidden = False
        for i in range(len(line)-1):
            if line[i] in vowels:
                vowelCount += 1

            if line[i:i+2] in forbiddens:
                forbidden = True

            if line[i] == line[i+1]:
                doubleLetter = True
        if line[-1] in vowels:
            vowelCount += 1

        if vowelCount >= 3 and doubleLetter and not forbidden:
            niceCount += 1

    print("Solution Part 1: ", niceCount)

def part2(filename: str) -> None:
    lines = get_lines(filename)

    niceCount = 0
    for line in lines:
        if len(line) <= 0:
            continue
        
        twoLetters = dict()
        twoLetter = False
        doubleLetter = False

        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                doubleLetter = True

        for i in range(len(line)-1):
            if line[i:i+2] in twoLetters:
                if i - twoLetters[line[i:i+2]] > 1:
                    twoLetter = True
            else:
                twoLetters[line[i:i+2]] = i

        if twoLetter and doubleLetter:
            niceCount += 1

    print("Solution Part 2: ", niceCount)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test2")
    part2("input1")

