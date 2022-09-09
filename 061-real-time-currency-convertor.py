from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()

print(c.get_rates('USD'))
print(c.get_rate('USD', 'BGN'))
print(c.convert('USD', 'BGN', 10))

b = BtcConverter()
print(b.get_latest_price('USD'))

codes = CurrencyCodes()
print(codes.get_symbol('EUR'))
