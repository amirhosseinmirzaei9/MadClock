from datetime import datetime
from clock_modes.morse import num_morse_code


def MadClock():
    time = datetime.now().strftime("%H:%M")
    mode_type = input("Which Mode : ").lower()
    if mode_type == "morse":
        output = list()
        for x in time:
            if x in num_morse_code:
                output.append(num_morse_code[x])
            elif x == ":":
                output.append("/")
        print(" ".join(output))
MadClock()
