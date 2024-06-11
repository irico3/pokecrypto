import sys


def command_line():
    args = sys.argv
    text: str = args[1]
    SPLIT_STEP = 3

    split_str = [text[i : i + SPLIT_STEP] for i in range(0, len(text), SPLIT_STEP)]
    return split_str
