import time
import os
import random
import math
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Clears the screen for Windows and Unix systems
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Displays text letter-by-letter
def display_letter_by_letter():
    text = "Hello, world!"
    for char in text:
        print(Fore.WHITE + char, end="", flush=True)
        time.sleep(0.2)
    time.sleep(2)    

# Displays text in a vertical line
def display_vertical():
    text = "Hello, world!"
    for char in text:
        print(Fore.WHITE + char, flush=True)
        time.sleep(0.1)  
    time.sleep(2)
    
# Flashes text on and off
def flash_text():
    text = "Bonjour, monde!"
    for _ in range(5): # Flash 5 times
        clear_screen()
        time.sleep(0.3)
        print(Fore.WHITE + text)
        time.sleep(0.3)
        
# Displays letters randomly
def display_randomly():
    text = "Hallo, Welt!"
    positions = list(range(len(text)))
    random.shuffle(positions)
    
    displayed = [" "] * len(text)
    for pos in positions:
        displayed[pos] = text[pos]
        print("".join(displayed), end="\r", flush=True)
        time.sleep(0.2)
    time.sleep(2)
    
# Typing effect with mistakes
def typing_effect():
    text = "Hello, world!"
    for char in text:
        if random.random() < 0.2:
            print(random.choice('abcdefghijklmnopqrstuvwxyz'), end="", flush=True)
            time.sleep(0.2)
            print("\b" + char, end="", flush=True)
        else:
            print(char, end="", flush=True)
        time.sleep(0.2)
    time.sleep(2)

# Matrix Effect
def matrix_effect():
    text = "Hello, world!"
    for _ in range(10):
        scrambled = ''.join(random.choice(text + "@#$%&*!?") for _ in text)
        print(Fore.GREEN + scrambled, end="\r", flush=True)
        time.sleep(0.1)
    print(Fore.WHITE + text)
    time.sleep(2)
    
# Fire Effect
def fire_effect():
    text = "Привет, мир!"
    colors = [Fore.RED, Fore.YELLOW, Fore.LIGHTYELLOW_EX]
    for _ in range(5):
        colored_text = ''.join(random.choice(colors) + char for char in text)
        print(colored_text, end="\r", flush=True)
        time.sleep(0.1)
    time.sleep(2)
    
# Shatter Effect
def shatter_effect():
    text = "Hello, world!"
    for _ in range(10):
        shattered = list(text)
        random.shuffle(shattered)
        print("".join(shattered), end="\r", flush=True)
        time.sleep(0.2)
    print(text)
    time.sleep(2)
    
# Blink Effect
def blink_effect():
    text = "Hello, world!"
    for _ in range(10):
        print(Fore.WHITE + text if _ % 2 == 0 else " ", end="\r", flush=True)
        time.sleep(0.3)
    time.sleep(2)
    
# Shadow Effect
def shadow_effect():
    text = "01001000 01100101 01101100 01101100 01101111 00101100 00100000 01110111 01101111 01110010 01101100 01100100 00100001"
    for _ in range(5):
        print(Fore.BLACK + " " * 2 + text)
        print(Fore.WHITE + text, end="\r", flush=True)
        time.sleep(0.3)
    time.sleep(2)
    
# Typing Deletion Effect
def typing_deletion_effect():
    text = "Hello, world!"
    for i in range(len(text) + 1):
        print(text[:i], end="\r", flush=True)
        time.sleep(0.1)
    time.sleep(1)
    for i in range(len(text), -1, -1):
        print(text[:i] + " ", end="\r", flush=True)
        time.sleep(0.1)
    time.sleep(2)
    
# Morse Code Effect
def morse_code_effect():
    morse_dict = { 'H': '....', 'e': '.', 'l': '.-..', 'o': '---', ',': '--..--', ' ': ' ', 'w': '.--', 'r': '.-.', 'd': '-..', '!': '-.-.--'}
    text = "Hello, world!"
    morse_text = ' '.join(morse_dict[char] for char in text if char in morse_dict)
    for symbol in morse_text:
        print(symbol, end="", flush=True)
        time.sleep(0.2)
    time.sleep(2)

# Earthquake Effect
def earthquake_effect():
    text = "Hello, world!"
    for _ in range(10):
        offset = " " * random.randint(0, 5)
        print(offset + text, end="\r", flush=True)
        time.sleep(0.1)
    time.sleep(2)

# Neon Glow Effect
def neon_glow_effect():
    text = "你好，世界！"
    colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX]
    for _ in range(10):
        print(random.choice(colors) + text, end="\r", flush=True)
        time.sleep(0.3)
    time.sleep(2)

# Countdown Reveal
def countdown_reveal():
    for i in range(3, 0, -1):
        print(Fore.RED + str(i), end="\r", flush=True)
        time.sleep(1)
    print(Fore.WHITE + "Hello, world!")
    time.sleep(2)

# Searchlight Effect
def searchlight_effect():
    text = "01001000 01100101 01101100 01101100 01101111 00101100 00100000 01110111 01101111 01110010 01101100 01100100 00100001"
    length = len(text)
    window_size = 2 # Size of highlight
    
    for _ in range(2):
        for i in range(length - window_size + 1):
            clear_screen()
            highlighted = (
                Fore.WHITE + text[i:i+window_size] +
                Fore.BLACK + text[i:window_size:]
            )
            print(Fore.BLACK + text[:i] + highlighted)
            time.sleep(0.2)
            
        for i in range(length - window_size - 1, -1, -1):
            clear_screen()
            highlighted = (
                Fore.WHITE + text[i:i+window_size] +
                Fore.BLACK + text[i:window_size:]
            )
            print(Fore.BLACK + text[:i] + highlighted)
            time.sleep(0.2)


def main():
	clear_screen()
	countdown_reveal()
	
	clear_screen()
	typing_effect()
	
	clear_screen()
	flash_text()
	
	clear_screen()
	display_randomly()
	
	clear_screen()
	shadow_effect()
	
	clear_screen()
	neon_glow_effect()
	
	clear_screen()
	matrix_effect()
	
	clear_screen()
	morse_code_effect()	
	
	clear_screen()
	fire_effect()
	
	clear_screen()
	typing_deletion_effect()
    
	clear_screen()
	print("Press Enter to exit...")
	input()
	
    
if __name__ == "__main__":
    main()
    
    

