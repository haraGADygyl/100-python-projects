import pyqrcode

url = "https://github.com/haraGADygyl/"

qr_code = pyqrcode.create(url)
qr_code.png("github.png", scale=10)
