from words import WORDS
from caesar_cipher import caesarCipher

def decode(s: str, n: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = ""
    for i in range(0, len(s)):
        if s[i].lower() in alphabet:
            index = alphabet.index(s[i].lower()) - n
            if index >= len(alphabet):
                index -= len(alphabet)
            res += alphabet[index]
        elif s[i] == " ":
            res += s[i]
    return res

def break_caesar(message):
    l = message.split(' ')
    possibleShifts = []
    for word in l:
        for i in range(1, 26):
            if decode(word.lower(), i) in WORDS:
                possibleShifts.append(i)
    highestOccurence = possibleShifts.count(possibleShifts[0])
    res = possibleShifts[0]
    for value in list(set(possibleShifts)):
        if possibleShifts.count(value) > highestOccurence:
            highestOccurence = possibleShifts.count(value)
            res = value
    return res
        


while True:
    answerText = input("Enter text to decypher ('q' to quit): ")
    if answerText.lower() == 'q':
        break
    shift = break_caesar(answerText)
    print(f'The most probable shift is: {shift}')
    decipheredText = caesarCipher(answerText, 'd', shift)
    print(f"Deciphered text: {decipheredText}")