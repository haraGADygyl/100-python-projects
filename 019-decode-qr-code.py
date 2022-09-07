from pyzbar.pyzbar import decode
from PIL import Image

decode_qr = decode(Image.open("resources/github.png"))

print(decode_qr[0].data.decode("ascii"))
