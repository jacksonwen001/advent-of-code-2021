# coding: utf-8 

from common.utils import read_files

def fishClock(fishes: dict, max_day: int) -> int:
    for day in range(1, max_day+1):
        old_fishes = fishes
        fishes = dict()
        for k, v in old_fishes.items():
            if( k == 0): 
                fishes[6] = fishes.get(6, 0) + v
                fishes[8] = fishes.get(8, 0) + v
                continue 
            fishes[k-1] = fishes.get(k-1, 0) + v
    sum = 0
    for count in fishes.values():
        sum += count
    return sum

if __name__ == "__main__":
    lines  = read_files("./inputs/day6")
    fishes = dict()

    lines = lines[0].split(",")

    for i in lines:
        fishes[int(i)] = lines.count(i)
    
    count = fishClock(fishes, 80)
    print("after 80 days: " + str(count))
    count = fishClock(fishes, 256)
    print("after 356 days: " + str(count))
