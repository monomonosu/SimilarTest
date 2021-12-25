from PIL import Image
import imagehash
import os

# 同じ画像データの比較であればハッシュ値は０となる

hash = imagehash.average_hash(Image.open('images/one.jpg'))
print(hash)

otherhash = imagehash.average_hash(Image.open('images/one.jpg'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)
