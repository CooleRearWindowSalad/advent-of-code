# Advent of Code 2025 - Solutions

This repository contains my **Advent of Code 2025** solutions, written in Python.  
Each day's puzzle has its own solution script and uses a separate input file (kept out of version control for privacy).

## Website
All puzzles come from [Advent of Code](https://adventofcode.com/).

---

## Project layout

advent-of-code/
- 2025/
  - advent1.py        # Day 1 solution
  - advent2.py        # Day 2 solution
  - ...               # More days
  - inputs/           # Input files (gitignored)
    - .txt
Notes:
- Each `advent.py` script is self-contained and reads its input from a `.txt` file in the same folder or in an `inputs/` subfolder.
- Input files are intentionally excluded from version control (globally ignored as `*.txt`) so puzzle inputs remain private.

---

## Usage

Open a PowerShell or Command Prompt in the repository root and run a day's script. Example:

```powershell
python .\advent-of-code\2025\advent2.py
```

The scripts will locate the appropriate input file (searching the folder and `inputs/` subfolder) and print the puzzle answers.

---

## Contributing / Notes

- These scripts are written as small, standalone solutions for personal use and learning. Suggestions are welcome.
- If you run them with your own inputs, place a `.txt` file alongside the script or inside the `inputs/` folder.

---

## License & Contact

This repository contains my personal solutions.  
If you need to reach me about this or any other project, please open a GitHub issue or contact me via my Discord 
username listed on my profile README.
