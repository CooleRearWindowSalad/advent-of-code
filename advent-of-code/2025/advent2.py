from pathlib import Path

def h(n):
    s = str(n)
    return len(s) % 2 == 0 and s[: len(s) // 2] == s[len(s) // 2:]

def r(n):
    s = str(n)
    return any(len(s) % k == 0 and s[:k] * (len(s) // k) == s for k in range(1, len(s) // 2 + 1))

def run(p):
    parts = [tuple(map(int, q.split("-"))) for q in Path(p).read_text().strip().split(",") if q.strip()]
    return (
        sum(v for A, B in parts for v in range(A, B + 1) if h(v)),
        sum(v for A, B in parts for v in range(A, B + 1) if r(v)),
    )

if __name__ == "__main__":
    folder = Path(__file__).parent
    a, b = run(sorted(folder.rglob("*.txt"))[1])
    print("Day 2 answer:", a)
    print("Part 2:", b)
