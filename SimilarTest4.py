from PIL import Image
import imagehash
import os

# 指定したオリジナル画像と一番類似する画像をリソースの中から検出する
# 人の服装で検証

originImage = '4.jpg'
otherHashDict = {}

hash = imagehash.average_hash(Image.open('clothesImages/'+originImage))
print(hash)

resourceImages = os.listdir('clothesImages')  # imagesディレクトリ内の画像名リスト取得
resourceImages.remove(originImage)  # オリジナルイメージをリストから外す
for image in resourceImages:
    otherHash = imagehash.average_hash(Image.open('clothesImages/'+image))
    hashdiff = hash-otherHash
    otherHashDict[image] = hashdiff  # イメージ名とハッシュ差のセットをDictに追加

print(otherHashDict)
minHashImageName = min(otherHashDict, key=otherHashDict.get)
print(minHashImageName)  # オリジナルイメージと一番近いハッシュ値のイメージ名を出力
