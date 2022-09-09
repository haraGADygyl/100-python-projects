import pyqrcode

url = 'https://thecleverprogrammer.com/2021/01/09/qr-codes-with-python/'

qr = pyqrcode.create(url)

qr.svg('resources/qr.svg', scale=8)
