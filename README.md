# SimilarTest
画像類似計算ライブラリのテスト
ImageHashというライブラリを使用してみる

## Pythonライブラリ
- ImageHash
   - 依存
      - numpy ◎直接依存？
      - Pillow 〇依存-依存関係？
      - PyWavelets ◎
      - scipy ◎
      - six 〇

## ImageHashインストール
pip install ImageHash

# 検証
結果数値が低いほど類似の判定。多いと別画像判定らしい。
完全一致でTRUE判定させるが、今回は同一人物でも別画像を使用しているので、無視。
## SimilarTest.py
画像単体同士で比較検証
### リゼロ：レム ⇔ リゼロ：レム
```
Python .\SimilarTest.py
1f1f1f1f1f1f3f6f
0b97f7617b130988
False
29
```

### リゼロ：レム ⇔ 無職転生：エリス

```
Python .\SimilarTest.py
1f1f1f1f1f1f3f6f
fc6466466227c640
False
40
```

レムりん同士で比較した方が数値が低いので、とりあえずは成功と言える。

## SimilarTest2.py
指定した画像とその他複数枚画像で比較検証

### リゼロ：レム ⇔ その他１０枚画像

```
Python .\SimilarTest2.py
1f1f1f1f1f1f3f6f
{'eight.jpg': 35, 'eleven.jpg': 44, 'five.jpg': 44, 'four.jpg': 26, 'nine.jpg': 39, 'seven.jpg': 23, 'six.jpg': 21, 'ten.jpg': 30, 'three.jpg': 40, 'two.png': 29}
six.jpg
```

複数画像の中からレムりんが選ばれるかと思ったが、結果はラムだった。
惜しいと言えば惜しい。
恐らくキャラの向いている方向。画像のエフェクトなどでも違いが出てくるのかもしれない。
