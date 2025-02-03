'''Hackerloader - a loader that reveals the selected text from the hackereffect.'''
import random

from charset import CHARSET


def hackerloader(string: str):
    '''The generator of hackereffect'''
    for char in range(len(string)):
        visible = string[0:char]
        hidden = string[char:len(string)]

        hidden = [random.choice(CHARSET) for _ in hidden]

        hidden = ''.join(hidden)
        yield visible+hidden


if __name__ == "__main__":
    word = "HACKING..."

    for stage in hackerloader(word):
        print(stage)
