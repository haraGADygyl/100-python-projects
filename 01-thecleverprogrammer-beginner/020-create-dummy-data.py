import pandas as pd
from faker import Faker

fake = Faker()

data = [fake.profile() for i in range(50)]
data = pd.DataFrame(data)

print(fake.name())
print(fake.address())
print(fake.text())

print(data.head())
