from PIL import Image
import imagehash

hash = imagehash.average_hash(Image.open('one.jpg'))
print(hash)

otherhash = imagehash.average_hash(Image.open('two.png'))
print(otherhash)

print(hash == otherhash)
print(hash - otherhash)
