def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str) -> None:
    lines = get_lines(filename)

    molecule = ""
    replacement_map = dict()
    for line in lines:
        if len(line) <= 0:
            continue

        if " => " not in line:
            molecule = line
            continue

        parts = line.split(" => ")
        if len(parts) != 2:
            print("Error: Invalid line")
            return

        fr = parts[0]
        to = parts[1]
        if fr not in replacement_map:
            replacement_map[fr] = [to]
        else:
            replacement_map[fr].append(to)

    if len(molecule) <= 0:
        print("Error: No molecule found")
        return

    molecules = set()
    for i in range(len(molecule)):
        part = molecule[i:i+2]

        if part in replacement_map:
            for to in replacement_map[part]:
                new_molecule = molecule[:i] + to + molecule[i+2:]
                molecules.add(new_molecule)
        elif part[0] in replacement_map:
            for to in replacement_map[part[0]]:
                new_molecule = molecule[:i] + to + molecule[i+1:]
                molecules.add(new_molecule)

    print("Solution Part 1: ", len(molecules))

def part2(filename: str) -> None:
    lines = get_lines(filename)

    molecule = ""
    replacements = []
    for line in lines:
        if len(line) <= 0:
            continue

        if " => " not in line:
            molecule = line
            continue

        parts = line.split(" => ")
        if len(parts) != 2:
            print("Error: Invalid line")
            return

        fr = parts[0]
        to = parts[1]
        if to not in replacements:
            replacements.append((fr, to))
        else:
            print("Error: Duplicate replacement")

    if len(molecule) <= 0:
        print("Error: No molecule found")
        return

    elements = sum(1 for c in molecule if c.isupper())
    brackets = molecule.count("Rn") + molecule.count("Ar")
    commas = molecule.count("Y")

    res = elements - brackets - 2 * commas - 1

    print("Solution Part 2: ", res)

if __name__ == "__main__":
    part1("test1")
    part1("input1")
    part2("test2")
    part2("input1")

