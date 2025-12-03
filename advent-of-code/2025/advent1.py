from pathlib import Path

def run(p):
    x = 50
    part1 = part2 = 0
    for inst in Path(p).read_text().split():
        d, v = inst[0], int(inst[1:])
        if d == "L":
            f = x or 100
            if v >= f: part2 += 1 + (v - f)//100
            x = (x - v) % 100
        else:
            f = (100 - x) % 100 or 100
            if v >= f: part2 += 1 + (v - f)//100
            x = (x + v) % 100
        part1 += x == 0
    return part1, part2

if __name__ == "__main__":
    folder = Path(__file__).parent
    p1, p2 = run(sorted(folder.rglob("*.txt"))[0])
    print("Day 1 Part 1 answer:", p1)
    print("Day 1 Part 2 answer:", p2)
