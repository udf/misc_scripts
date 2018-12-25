from sys import argv
from base64 import b64encode
import json


def hex_esc(c):
    return f'&#x{ord(c):X};'


def main():
    if len(argv) != 3:
        raise RuntimeError(f"Usage: python {argv[0]} [question] [answer]")
    output = json.dumps({
            "q": argv[1],
            "a": [hex_esc(c) for c in argv[2]]
    })
    print(output)
    print(f'https://xkcd.com/1525/#{b64encode(output.encode("ascii")).decode("ascii")}')


if __name__ == '__main__':
    try:
        main()
    except RuntimeError as e:
        print(e)
        exit(1)
