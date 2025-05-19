from datetime import datetime
from clock_modes.morse import num_morse_code


class MadClock:
    def __init__(self):
        self.time = datetime.now().strftime("%H:%M")

    def run(self):
        mode_type = input("Which Mode: ").lower()
        if mode_type == "morse":
            self.show_morse()

    def show_morse(self):
        output = []
        for char in self.time:
            if char in num_morse_code:
                output.append(num_morse_code[char])
            elif char == ":":
                output.append("/")
        print(" ".join(output))


if __name__ == "__main__":
    clock = MadClock()
    clock.run()
