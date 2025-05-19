from datetime import datetime
from clock_modes.morse import num_morse_code


class MadClock:
    def __init__(self):
        self.time = datetime.now().strftime("%H:%M")

    def run(self):
        mode_type = input("Which Mode: ").lower()
        if mode_type == "morse":
            self.show_morse()
        elif mode_type == "binary":
            self.show_binary()
        elif mode_type == "reverse":
            self.show_reverse()

    def show_morse(self):
        output = []
        for char in self.time:
            if char in num_morse_code:
                output.append(num_morse_code[char])
            elif char == ":":
                output.append("/")
        print(" ".join(output))


    def show_binary(self):
        output = list()
        for char in self.time:
            if char.isdigit():
                output.append(bin(int(char))[2:])
            elif char == ":":
                output.append("/")
        print(" ".join(output))


    def show_reverse(self):
        hour, minute = self.time.split(":")
        reversed_hour = hour[::-1]
        reversed_minute = minute[::-1]
        print(f"{reversed_minute}:{reversed_hour}")


if __name__ == "__main__":
    clock = MadClock()
    clock.run()
