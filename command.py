import re
import sys

from lib.split_str import split_str

SPLIT_STEP = 3


def make_split_str():
    try:
        args = sys.argv
        text: str = args[1]
        if not re.search(r"[ぁ-ゔ]+|[ー]+", text):
            raise IndexError

        str_list = split_str(text, SPLIT_STEP)
        return str_list
    except IndexError:
        print("正しい文字を入力してください。ひらがなのみ対応しています。")
        sys.exit()
