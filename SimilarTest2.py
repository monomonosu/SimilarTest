from PIL import Image
import imagehash
import os

# 指定したオリジナル画像と一番類似する画像をリソースの中から検出する

originImage = 'one.jpg'
otherHashDict = {}

hash = imagehash.average_hash(Image.open('images/'+originImage))
print(hash)

resourceImages = os.listdir('images')  # imagesディレクトリ内の画像名リスト取得
resourceImages.remove(originImage)  # オリジナルイメージをリストから外す
for image in resourceImages:
    otherhash = imagehash.average_hash(Image.open('images/'+image))

    hashdiff = hash-otherhash

    otherHashDict[image] = hashdiff

print(otherHashDict)
minHashImageName = min(otherHashDict, key=otherHashDict.get)
print(minHashImageName)
