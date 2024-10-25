MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter.upper() in MORSE_CODE_DICT:
            cipher += MORSE_CODE_DICT[letter.upper()] + ''
        else:
            cipher += ""
    return cipher

def main():
    keep_running = True
    while keep_running:
        message = input("Enter Your message: ")
        if message.lower() == "exit":
            keep_running = False
            print("Exiting...")
        else:
            result = encrypt(message)
            print("Morse Code:", result)


if __name__ == "__main__":
    main()