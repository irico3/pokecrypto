def split_str(str: str, split_step: int):
    split_str = [str[i : i + split_step] for i in range(0, len(str), split_step)]
    return split_str
