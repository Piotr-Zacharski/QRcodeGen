import qrcode
from PIL import Image

add_url = input("Podaj nazwę strony: ")
filename = input("Podaj nazwę pliku z rozszerzeniem: ")

img = qrcode.make(add_url)
img.save(filename)
opener = Image.open(filename)
opener.show()
