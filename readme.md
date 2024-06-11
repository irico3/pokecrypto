# pokecrypto

MIT License

ポケモンの図鑑解説を用いて暗号を生成するプログラムです。

```
python index.py 暗号化する文字列
```

暗号化する文字列は現在ひらがなのみサポートしています。

## example

入力

```
python index.py ぽけもん
```

出力

```
x643/41-43x188/20-20
```

x -> 図鑑バージョン
643 -> ポケモン No
41-43 -> 文字の位置
a

といった形で繰り返し文字を置換します。
