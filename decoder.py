#Decoding QrCode
from pyzbar.pyzbar import decode
from PIL import image #(Pillow)

img = Image.open('C:/User/')
result = decode(img)
print(result)