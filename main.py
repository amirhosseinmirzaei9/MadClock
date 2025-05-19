from datetime import datetime
from clock_modes.morse import num_morse_code


class MadClock:
    def get_time(self):
        return datetime.now().strftime("%H:%M")

    def run(self):
        while True:
            mode_type = input("Which Mode (or 'exit' to quit): ").lower()
            if mode_type == "morse":
                self.show_morse()
            elif mode_type == "binary":
                self.show_binary()
            elif mode_type == "reverse":
                self.show_reverse()
            elif mode_type == "exit":
                print("Goodbye!")
                break
            else:
                print("Invalid mode. Please choose from: morse, binary, reverse.")

    def show_morse(self):
        time = self.get_time()
        output = []
        for char in time:
            if char in num_morse_code:
                output.append(num_morse_code[char])
            elif char == ":":
                output.append("/")
        print(" ".join(output))

    def show_binary(self):
        time = self.get_time()
        output = []
        for char in time:
            if char.isdigit():
                output.append(format(int(char), "04b"))
            elif char == ":":
                output.append("/")
        print(" ".join(output))

    def show_reverse(self):
        time = self.get_time()
        hour, minute = time.split(":")
        reversed_hour = hour[::-1]
        reversed_minute = minute[::-1]
        print(f"{reversed_minute}:{reversed_hour}")


if __name__ == "__main__":
    clock = MadClock()
    clock.run()
