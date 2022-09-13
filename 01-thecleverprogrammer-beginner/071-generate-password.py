import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

print(''.join(random.sample(characters, 10)))
