from pathlib import Path

def m(line, k):
    d = [c for c in line if c.isdigit()]
    if len(d) < k: return 0
    r, s = [], 0
    for i in range(k):
        b = max(range(s, len(d) - k + i + 1), key=lambda j: d[j])
        r.append(d[b])
        s = b + 1
    return int(''.join(r))

def run(p):
    lines = [l.strip() for l in Path(p).read_text().splitlines() if l.strip()]
    return sum(m(l, 2) for l in lines), sum(m(l, 12) for l in lines)

if __name__ == "__main__":
    folder = Path(__file__).parent
    p1, p2 = run(sorted(folder.rglob("*.txt"))[2])
    print("Part 1:", p1)
    print("Part 2:", p2)
