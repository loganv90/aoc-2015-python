def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def part1(filename: str, total_time: int) -> None:
    lines = get_lines(filename)

    map = {}
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        if len(split) != 15:
            raise ValueError("Invalid line")

        name = split[0]
        speed = int(split[3])
        time = int(split[6])
        rest = int(split[13])

        map[name] = (speed, time, rest)

    distances = {}
    going = {}
    stopped = {}
    for name in map:
        distances[name] = 0
        going[name] = 0
        stopped[name] = 0

    for _ in range(total_time):
        for name in map:
            speed, time, rest = map[name]

            time_going = going[name]
            time_stopped = stopped[name]

            if time_going < time:
                going[name] += 1
                distances[name] += speed
            elif time_stopped < rest:
                stopped[name] += 1
            else:
                going[name] = 1
                stopped[name] = 0
                distances[name] += speed

    max_distance = 0
    for name in distances:
        if distances[name] > max_distance:
            max_distance = distances[name]

    print("Solution Part 1: ", max_distance)

def part2(filename: str, total_time: int) -> None:
    lines = get_lines(filename)

    map = {}
    for line in lines:
        if len(line) <= 0:
            continue

        split = line.split(" ")
        if len(split) != 15:
            raise ValueError("Invalid line")

        name = split[0]
        speed = int(split[3])
        time = int(split[6])
        rest = int(split[13])

        map[name] = (speed, time, rest)

    distances = {}
    going = {}
    stopped = {}
    points = {}
    for name in map:
        distances[name] = 0
        going[name] = 0
        stopped[name] = 0
        points[name] = 0

    for _ in range(total_time):
        for name in map:
            speed, time, rest = map[name]

            time_going = going[name]
            time_stopped = stopped[name]

            if time_going < time:
                going[name] += 1
                distances[name] += speed
            elif time_stopped < rest:
                stopped[name] += 1
            else:
                going[name] = 1
                stopped[name] = 0
                distances[name] += speed

        max_distance = 0
        max_names = []
        for name in distances:
            if distances[name] > max_distance:
                max_distance = distances[name]
                max_names = [name]
            elif distances[name] == max_distance:
                max_names.append(name)

        for max_name in max_names:
            points[max_name] += 1

    max_points = 0
    for name in points:
        if points[name] > max_points:
            max_points = points[name]

    print("Solution Part 2: ", max_points)

if __name__ == "__main__":
    part1("test1", 1)
    part1("test1", 10)
    part1("test1", 11)
    part1("test1", 12)
    part1("test1", 138)
    part1("test1", 174)
    part1("test1", 1000)
    part1("input1", 2503)
    part2("test1", 1000)
    part2("input1", 2503)

