product1_name, product1_price = 'Books', 50.95
product2_name, product2_price = 'Computer', 598.99
product3_name, product3_price = 'Monitor', 156.89

company_name = 'Thecleverprogrammer, inc.'
company_address = '144 Kalka ji.'
company_city = 'New Delhi'

print('*' * 50, end='\n\n')
print(f'\t{company_name}\n\t{company_address}\n\t{company_city}')
print('=' * 50)
print(f'\tProduct Name\tProduct Price')
print(f'\t{product1_name}\t\t\t${product1_price}')
print(f'\t{product2_name}\t\t${product2_price}')
print(f'\t{product3_name}\t\t\t${product3_price}')
print('=' * 50)
print(f'\t\t\t\t\tTotal\n\t\t\t\t\t${product1_price + product2_price + product3_price}')
print('=' * 50)
print('\n\t\tThank you for shopping with us!\n')
print('*' * 50, end='\n\n')
