from PIL import Image
import imagehash

# 指定した画像同士を比較する単純なもの

hash = imagehash.average_hash(Image.open('images/one.jpg'))
print(hash)

otherhash = imagehash.average_hash(Image.open('images/two.png'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)
