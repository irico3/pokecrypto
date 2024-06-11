import re
import sys

SPLIT_STEP = 3


def make_split_str():
    try:
        args = sys.argv
        text: str = args[1]
        if not re.search(r"[ぁ-ゔ]+|[ー]+", text):
            raise IndexError

        split_str = [text[i : i + SPLIT_STEP] for i in range(0, len(text), SPLIT_STEP)]
        return split_str
    except IndexError:
        print("正しい文字を入力してください。ひらがなのみ対応しています。")
        sys.exit()
