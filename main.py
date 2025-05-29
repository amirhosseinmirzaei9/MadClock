from datetime import datetime
from colorama import init, Fore, Style
from pyfiglet import Figlet
from clock_modes.morse import num_morse_code
import time
import json
import os
import random



MODES = ["morse", "binary", "typewriter", "reverse", "hex", "reminder", "live", "clear", "digital","format", "exit", "help", "ascii"]

init(autoreset=True)

class MadClock:
    def __init__(self):
        self.time_format = "12h" 
        
    def get_time(self):
        if self.time_format == "12h":
            return datetime.now().strftime("%I:%M %p")
        else:
            return datetime.now().strftime("%H:%M")

    def run(self):
        while True:
            mode_type = input("Which Mode (or 'exit' to quit): ").strip().lower()
            if mode_type == "morse":
                self.show_morse()
            elif mode_type == "binary":
                self.show_binary()
            elif mode_type == "format":
                self.toggle_format()
            elif mode_type == "reverse":
                self.show_reverse()
            elif mode_type == "live":
                self.show_live_clock()
            elif mode_type == "hex":
                self.show_hex()
            elif mode_type == "clear":
                self.clear()
            elif mode_type == "ascii":
                self.show_ascii()
            elif mode_type == "typewriter":
                self.show_typewriter()
            elif mode_type == "help":
                self.show_help()
            elif mode_type == "digital":
                self.show_digital()
            elif mode_type == "exit":
                msg = "Goodbye!!!"
                for char in msg:
                    print(Fore.GREEN + char, end="", flush=True)
                    time.sleep(0.2)
                time.sleep(0.3)
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print(Fore.RED + "Invalid mode. Please choose from:")
                print(Fore.YELLOW + ", ".join(MODES))
    
    def show_morse(self):
        time = self.get_time()
        output = []
        for char in time:
            if char in num_morse_code:
                output.append(num_morse_code[char])
            elif char == ":":
                output.append("/")
        print(Fore.YELLOW + " ".join(output))

    def show_binary(self):
        time = self.get_time()
        output = []
        for char in time:
            if char.isdigit():
                output.append(format(int(char), "04b"))
            elif char == ":":
                output.append("/")
        print(Fore.GREEN + " ".join(output))

    
    def show_reverse(self):
        time = self.get_time()
        time_part = time.split(" ")[0]  
        suffix = time.split(" ")[1] if self.time_format == "12h" else ""
        hour, minute = time_part.split(":")
        reversed_hour = hour[::-1]
        reversed_minute = minute[::-1]
        print(Fore.BLUE + f"{reversed_minute}:{reversed_hour} {suffix}".strip())
    
    def toggle_format(self):
        if self.time_format == "24h":
            self.time_format = "12h"
        else:
            self.time_format = "24h"
        print(Fore.MAGENTA + f"Switched to {self.time_format.upper()} Format")
        
        
    def show_live_clock(self):
        try:
            os.system("cls" if os.name == "nt" else "clear")
            while True:
                print(f"\r{self.get_time():<12}", end="", flush=True)
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n" + Fore.RED + "Live clock stopped. Returning to main menu....")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")

    
    def show_hex(self):
        time = self.get_time().split(" ")[0]
        output = []
        for char in time:
            if char.isdigit():
                output.append(hex(int(char))[2:].upper())
            elif char == ":":
                output.append("/")
        print(Fore.LIGHTMAGENTA_EX + " ".join(output))

    def show_ascii(self):
        time_str = self.get_time()
        fonts = ["epic" , "slant", "big", "digital", "block", "chunky"]
        f = Figlet(font=random.choice(fonts))
        print(Fore.LIGHTCYAN_EX + f.renderText(time_str))

    def show_help(self):
        help_text = {
            "morse": "Display time in Morse code.",
            "binary": "Display time in binary format.",
            "reverse": "Reverse hour and minute.",
            "hex": "Display time digits in hexadecimal.",
            "ascii": "Display time in large ASCII art.",
#            "reminder": "Set a time reminder that alerts you when the time comes.",
            "digital": "Display time in digital format with seconds.",
            "typewriter": "Show the clock in a typewriter-style typing effect.",
            "live": "Show a live updating clock.",
            "format": "Toggle between 12h and 24h formats.",
            "clear" : "Clearing terminal Page",
            "exit" : "Exit the clock app.",
        }
        print(Fore.CYAN + "\nAvailable Modes:")
        for k, v in help_text.items():
            print(Fore.YELLOW + f"  {k:8} ➜ {v}")   

    def show_digital(self):
        print(Fore.LIGHTYELLOW_EX + datetime.now().strftime("%H:%M:%S"))

    def show_typewriter(self):
        time_str = self.get_time()
        print(Fore.GREEN + "Typing time...", end="", flush=True)
        for char in time_str:
            print(Fore.GREEN + char, end="", flush=True)
            time.sleep(0.1)
        print()
        print(Fore.GREEN + "Done!")

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    clock = MadClock()
    clock.run()

