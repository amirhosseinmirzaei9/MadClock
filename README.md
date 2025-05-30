
# Mad Clock 🕰️

**Mad Clock** is an interactive terminal clock that displays the current time in various creative and fun formats!  
From Morse code and binary to typewriter effects and ASCII art, this clock offers multiple unique modes to visualize the time.

## Features

- Toggle between 12-hour and 24-hour time formats
- Multiple display modes, including:
    - **Morse**: Shows time in Morse code
    - **Binary**: Displays time digits in binary
    - **Reverse**: Reverses hour and minute digits
    - **Hex**: Shows time digits in hexadecimal
    - **ASCII**: Displays time as large ASCII art with different fonts
    - **Typewriter**: Types out the time with typewriter sound effect
    - **Live**: Real-time updating clock display
    - **Digital**: Shows digital clock with seconds
    - **Random**: Randomly selects a display mode each time
- Clear terminal screen command
- Help command to list all available modes
- Exit command to quit the program

## Requirements

- Python 3.6 or higher
- [colorama](https://pypi.org/project/colorama/)
- [pyfiglet](https://pypi.org/project/pyfiglet/)
- [pygame](https://pypi.org/project/pygame/)

Install dependencies with:

```Bash
pip install colorama pyfiglet pygame
```

## How to Run

1. Clone or download this repository.
2. Open a terminal and navigate to the project folder.
3. Run the clock with:

```Bash
python main.py
```

4. Enter one of the following modes:
	- `morse` 
	- `binary` 
	- `typewriter` 
	- `reverse` 
	- `random` 
	- `hex` 
	- `live` 
	- `clear` 
	- `digital` 
	- `format` 
	- `exit` 
	- `help` 
	- `ascii`
5. Type `help` to display descriptions of each mode.
6. Type `exit` to quit the program.


## Usage

After running the program, enter one of the mode commands to see the time displayed in that style.  
In **live** mode, the clock updates every second until you press `Ctrl+C` to return to the main menu.



## Future Improvements

You can extend this project by adding:

- Timer and stopwatch features
- World clocks for different time zones
- Reminder/alert functionality
- Additional fun and creative time display modes



## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.