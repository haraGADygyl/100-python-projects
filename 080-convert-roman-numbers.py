tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def roman_to_decimal(r):
    total = 0

    for i in range(len(r) - 1):
        left = r[i]
        right = r[i + 1]

        if tallies[left] < tallies[right]:
            total -= tallies[left]
        else:
            total += tallies[left]

    total += tallies[r[-1]]
    return total


print(roman_to_decimal('XIX'))
