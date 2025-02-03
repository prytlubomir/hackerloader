import random

from charset import CHARSET


def hackerloader(string: str):
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
