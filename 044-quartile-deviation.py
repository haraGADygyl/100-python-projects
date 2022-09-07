import numpy as np

data = [x for x in range(20, 100, 5)]

q1 = np.quantile(data, 0.25)
q2 = np.quantile(data, 0.50)
q3 = np.quantile(data, 0.75)

print(f'Quantile 1: {q1}')
print(f'Quantile 2: {q2}')
print(f'Quantile 3: {q3}')


def quantile_deviation(qu1, qu3):
    return (qu3 - qu1) / 2


print(quantile_deviation(q1, q3))
