from pathlib import Path

def run(p):
    z = x = 50
    for i in Path(p).read_text().split():
        x = (x - int(i[1:])) % 100 if i[0] == "L" else (x + int(i[1:])) % 100
        z += x == 0
    return z

if __name__ == "__main__":
    folder = Path(__file__).parent
    txt_files = sorted(folder.rglob("*.txt"))
    input_file = txt_files[0]
    print("Day 1 answer:", run(input_file))