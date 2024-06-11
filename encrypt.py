import random

from gql_execute import gql_execute
from lib.split_str import split_str


def encrypt(str: str, encrypt_list):
    result = gql_execute(str)
    result_count = len(result)
    if result_count == 0:
        # 一文字ずつ切り崩して再度暗号化
        if len(str) == 1:
            raise RuntimeError("文字が見つかりませんでした。: " + str)
        splitted = split_str(str, len(str) - 1)
        for s in splitted:
            encrypt(s)
    else:
        print("平文: " + str)

        random_index = random.randrange(result_count)
        pick_result = result[random_index]
        flavor_text = pick_result["flavor_text"]
        formatted = flavor_text.replace("\n", "").replace("\u3000", "")
        print("解説文: " + formatted)

        flavor_index = formatted.find(str)
        version_name = pick_result["pokemon_v2_version"]["name"]
        id = pick_result["pokemon_species_id"]
        encrypt_text = (
            f"{version_name}{id}/{flavor_index}-{flavor_index +(len(str) - 1)}"
        )
        encrypt_list.append(encrypt_text)
        print("暗号化: " + encrypt_text)
