[![Tests](https://github.com/crowz-fx/sudoku_solver/actions/workflows/install-and-test.yaml/badge.svg)](https://github.com/crowz-fx/sudoku_solver/actions/workflows/install-and-test.yaml)

# sudoku_solver
Python application to solve sudoku puzzles

## Info
Sudoku solver that can operate in two modes `headless` and `gui`

### Common
- Solves sudoku duh!
- Displays time taken to solve
- Operation counts

### GUI 
- Ability to input a puzzle to be solved
- Can generate a new puzzle that you can input or ask to be solved

![gui demo](media/gui.gif)

### Headless
- Can supply a puzzle in two ways
  - `oneliner` - one continuous csv string of the puzzle
    - ![headless oneliner demo](media/headless_oneliner.gif)
  - `file` - file with puzzle within 
    - ![headless file demo](media/headless_file.gif)
- Will output the solved puzzle to either console or a file depending on parameter supplied

## Compatability
Built and tested with python `3.11.6`, all dependencies are frozen and pinned in [requirements.txt](requirements.txt)

## Running
Follow the steps in [Setup](#setup) first

## Help
There is argument parsing at all levels, just tack on -h to see usage instructions, examples:
```bash
python main.py -h
python main.py gui -h
python main.py headless oneliner -h
```

### GUI
```bash
python main.py gui
```

### Headless
#### OneLiner
```bash
python main.py headless oneliner 0,0,1,2,6,0...
```

#### File
```bash
python main.py headless file puzzle.txt
```

## Setup
1. Setup python virtual environment
```bash
python -m venv venv
```
2. Activate and install dependencies
```bash
source venv/bin/activate && \
pip3 install -r requirements.txt
```

## Executing Tests
```bash
python -m unittest discover -s tests -v
```
