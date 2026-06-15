# Rock-Paper-Scissors Python Project

This repository contains a step-by-step implementation of the classic **Rock-Paper-Scissors** game in Python, based on the [WiredIn Academy](https://github.com/techgymjp/techgym_python_en) curriculum.

## Prerequisites

- Python 3.x

## Curriculum Outline

Each folder contains a single exercise with increasing difficulty, building from basic input handling up to a fully functionalized game using lists and dictionaries.

### Structure

| Folder / File              | Task                         | Description |
|----------------------------|------------------------------|-------------|
| `1-1_add_paper/`           | `y5YT.py`                    | adding "paper" to an initial rock-scissors game |
| `1-2_determine_outcome/`   | `v7Pi.py`                    | implementing win/lose/draw logic using if/elif/else |
| `1-3_functionalization/`   | `a5Qm.py`                    | splitting logic into reusable functions |
| `1-4_display_hand/`        | `gP6s.py`                    | showing player/computer choices as text (rock/scissors/paper) |
| `1-5_use_list_input/`      | `dV9E.py`                    | using a list to format input prompt dynamically |
| `1-6_use_dict_result/`     | `L2rT.py`                    | using a dictionary to format game results |
| `1-7_repeat_draw/`         | `Jv5e.py`                    | repeating the game until there is a winner |
| `main.py` (root)           | run the final game           | entry point to play the final version without navigating folders |

## Concepts Covered

| Concept                  | Introduced in  |
|--------------------------|----------------|
| `random.randint()`       | Step 1-1       |
| `if/elif/else` chains    | Step 1-2       |
| Functions                | Step 1-3       |
| List indexing            | Step 1-4       |
| Passing data via args    | Step 1-5       |
| Dictionary lookups       | Step 1-6       |
| Recursion                | Step 1-7       |
| Dynamic module loading   | `main.py`      |

---

## How to Play

Run `main.py` from the root of the repository:

```bash
python main.py
```

You will be prompted to enter a number for your hand:

```
0: rock  1: scissors  2: paper
your hand:
```

If the result is a draw, the game repeats automatically until there is a winner.

## Known Limitations

- **No input validation** — entering a non-integer (e.g. typing `rock`) raises a `ValueError` and crashes the program.
- **Recursion on draw** — the final version uses recursion instead of a loop. With an unlikely but theoretically unbounded sequence of draws, this could hit Python's default recursion limit of 1000.
