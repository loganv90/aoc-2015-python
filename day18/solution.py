def get_lines(filename: str) -> list[str]:
    file = open(filename, "r")
    text = file.read()
    lines = text.split("\n")
    return lines

def print_grid(grid: list[list[bool]]) -> None:
    print()
    print("grid:")
    for row in grid:
        for cell in row:
            if cell:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def get_next_grid(grid: list[list[bool]]) -> list[list[bool]]:
    count_grid = []
    next_grid = []
    for row in grid:
        count_row = []
        next_row = []
        for _ in row:
            count_row.append(0)
            next_row.append(False)
        count_grid.append(count_row)
        next_grid.append(next_row)

    for row in range(len(grid)):
        for col in range(len(grid)):
            for count_row in range(max(0, row-1), min(len(grid), row+2)):
                for count_col in range(max(0, col-1), min(len(grid), col+2)):
                    if count_row == row and count_col == col:
                        continue
                    if grid[count_row][count_col]:
                        count_grid[row][col] += 1

    for row in range(len(grid)):
        for col in range(len(grid)):
            state = grid[row][col]
            count = count_grid[row][col]

            if state:
                if count == 2 or count == 3:
                    next_grid[row][col] = True
            else:
                if count == 3:
                    next_grid[row][col] = True

    return next_grid

def count_grid(grid: list[list[bool]]) -> int:
    count = 0
    for row in grid:
        for cell in row:
            if cell:
                count += 1
    return count

def part1(filename: str, steps: int) -> None:
    lines = get_lines(filename)

    grid: list[list[bool]] = []
    for line in lines:
        if len(line) <= 0:
            continue

        row: list[bool] = []
        for char in line:
            if char == "#":
                row.append(True)
            else:
                row.append(False)
        grid.append(row)

    for _ in range(steps):
        grid = get_next_grid(grid)
    
    print("Solution Part 1: ", count_grid(grid))

def part2(filename: str, steps: int) -> None:
    lines = get_lines(filename)

    grid: list[list[bool]] = []
    for line in lines:
        if len(line) <= 0:
            continue

        row: list[bool] = []
        for char in line:
            if char == "#":
                row.append(True)
            else:
                row.append(False)
        grid.append(row)

    grid[0][0] = True
    grid[0][len(grid)-1] = True
    grid[len(grid)-1][0] = True
    grid[len(grid)-1][len(grid)-1] = True
    for _ in range(steps):
        grid = get_next_grid(grid)
        grid[0][0] = True
        grid[0][len(grid)-1] = True
        grid[len(grid)-1][0] = True
        grid[len(grid)-1][len(grid)-1] = True
    
    print("Solution Part 2: ", count_grid(grid))

if __name__ == "__main__":
    part1("test1", 4)
    part1("input1", 100)
    part2("test2", 5)
    part2("input1", 100)

