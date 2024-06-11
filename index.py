from command import make_split_str
from encrypt import encrypt


def main():
    print("ポケモン暗号化プログラム")
    split_str = make_split_str()
    encrypt_list = []
    for str in split_str:
        encrypt(str, encrypt_list)

    encrypt_line = "".join(encrypt_list)
    print("暗号結果", encrypt_line)
    return encrypt_line


main()
