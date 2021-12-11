# coding: utf-8 

def read_files(name: str) -> list:
    with open(name, "r") as f:
        lines  = f.readlines()
    return lines


if __name__ == "__main__":
    lines = read_files("./inputs/day5")
    print(lines)