import qrcode
from PIL import Image
import tkinter as tk


root = tk.Tk()
root.title("QRcodeGen")

add_url = input("Podaj nazwę strony: ")
filename = input("Podaj nazwę pliku z rozszerzeniem: ")

canvas = tk.Canvas(root, width=600, height=400)
canvas.grid(columnspan=3)

url = tk.Entry(root).grid(columnspan=1, column=0, row=1)
#url
extension = tk.Entry(root).grid(columnspan=1, column=1, row=2)
#extension

img = qrcode.make(add_url)
img.save(filename)
opener = Image.open(filename)
opener.show()

root.mainloop()
