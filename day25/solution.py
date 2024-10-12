def get_index(row: int, col: int) -> int:
    diagonal = (row - 1) + (col - 1) + 1

    index = col
    for i in range(1, diagonal):
        index += i

    return index

def part1(row: int, col: int, code: int) -> None:
    index = get_index(row, col)

    for _ in range(1, index):
        code = (code * 252533) % 33554393

    print("Solution Part 1: ", code)

if __name__ == "__main__":
    part1(6, 2, 20151125)
    part1(2981, 3075, 20151125)

