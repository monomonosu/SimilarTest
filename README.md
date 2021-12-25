# SimilarTest
画像類似計算ライブラリのテスト

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

## 検証
結果数値が低いほど類似の判定。多いと別画像判定らしい。
完全一致でTRUE判定させるが、今回は同一人物でも別画像を使用しているので、無視。
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