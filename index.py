import requests

print("ポケモン暗号化プログラム")
text = input("暗号化したい文字列をひらがなで入力してください: ")

print(text)

SPLIT_STEP = 2
split_str = [text[i : i + SPLIT_STEP] for i in range(0, len(text), SPLIT_STEP)]

print(split_str)


url = "http://xxxxx"
payload = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params=payload)
