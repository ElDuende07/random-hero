# Random Hero

Random Hero is a Python program that randomly selects a hero from the full Dota 2 hero pool while avoiding repeated selections.

Dota 2 includes a random-selection button, but its selection cannot be changed. This project allows the user to continue choosing random heroes without receiving the same hero twice. After every hero has been selected, the saved history resets automatically.

## Features

- Selects a random Dota 2 hero
- Prevents previously selected heroes from repeating
- Saves selection history locally
- Downloads and displays the selected hero's image
- Allows the user to continue, reset the history, or exit

## Requirements

- Python 3.10 or newer
- Requests
- Pillow

## Installation

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the program

Run:

```bash
python main.py
```

The program displays a hero's name and attempts to open the hero's image. Enter `y` to choose another hero, enter `reset` to clear the selection history, or enter any other value to exit.

The program creates `used_heroes.txt` automatically to store selection history. This local history file is excluded from GitHub.

## Technologies

- Python
- Requests
- Pillow
- Dota 2 public image CDN

## Authors

- Alberto Lopez
- Yosbel Gonzalez
