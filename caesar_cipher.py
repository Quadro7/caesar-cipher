from os import system

def caesarCipher(text: str, mode: str, shift: int) -> str:
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    ciphered_text = ''
    for symbol in text:
        if symbol in ascii_lowercase:
            if mode == 'e' or mode == 'encode':
                index = (ascii_lowercase.index(symbol) + shift) % len(ascii_lowercase)
            elif mode == 'd' or mode == 'decode':
                index = ascii_lowercase.index(symbol) - shift
            ciphered_text += ascii_lowercase[index]
        elif symbol in ascii_uppercase:
            if mode == 'e' or mode == 'encode':
                index = (ascii_uppercase.index(symbol) + shift) % len(ascii_uppercase)
            elif mode == 'd' or mode == 'decode':
                index = ascii_uppercase.index(symbol) - shift
            ciphered_text += ascii_uppercase[index]
        elif symbol in digits:
            if mode == 'e' or mode == 'encode':
                index = (digits.index(symbol) + shift) % len(digits)
            elif mode == 'd' or mode == 'decode':
                index = (digits.index(symbol) - shift) % len(digits)
            ciphered_text += digits[index]
        else:
            ciphered_text += symbol
    return ciphered_text


if __name__ == "__main__":
    LOGO = '''
     _____                              _____ _       _               
    /  __ \                            /  __ (_)     | |              
    | /  \/ __ _  ___  ___  __ _ _ __  | /  \/_ _ __ | |__   ___ _ __ 
    | |    / _` |/ _ \/ __|/ _` | '__| | |   | | '_ \| '_ \ / _ \ '__|
    | \__/\ (_| |  __/\__ \ (_| | |    | \__/\ | |_) | | | |  __/ |   
     \____/\__,_|\___||___/\__,_|_|     \____/_| .__/|_| |_|\___|_|   
                                               | |                    
                                               |_|                    '''
    isRunning = True

    while isRunning:
        system('clear')
        print(LOGO)
        modeAnswer = input('[d]ecode or [e]ncode? ').lower()
        if modeAnswer == 'd' or modeAnswer == 'decode':
            textAnswer = input('Text to decode: ')
        elif modeAnswer == 'e' or modeAnswer == 'encode':
            textAnswer = input('Text to encode: ')
        else:
            continue
        shiftAmount = int(input('Enter shift (between 1 and 25): '))
        cipheredText = caesarCipher(text=textAnswer, mode=modeAnswer, shift=shiftAmount)
        print(f'Here is ciphered text: {cipheredText}')
        runAgain = input('Run again? [y]es / [n]o: ').lower()
        if runAgain == 'n' or runAgain == 'no':
            isRunning = False
