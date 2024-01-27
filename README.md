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

TODO - add screenshot

### Headless
- Can supply a puzzle in a <b>oneliner</b> parameter or from a file
- Will output the solved puzzle to either console or a file depending on parameter supplied

TODO - add screenshot

## Compatability
Built and tested with python `3.11.6`, all dependencies are frozen and pinned in [requirements.txt](requirements.txt)

## Running
Follow the steps in [Setup](#setup) first
### GUI
```bash
python3 ... TODO - add
```

### Headless
```bash
python3 ... TODO - add
```

## Setup
1. Setup python virtual environment
```bash
python3 -m venv venv
```
2. Activate and install dependencies
```bash
source venv/bin/activate && \
pip3 install -r requirements.txt
```