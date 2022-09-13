def larger_than(a, b):
    if a == b:
        return False

    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False

    for d in range(len(a)):
        if a[d] < b[d]:
            return False

    return True


print(larger_than('112', '111'))
print(larger_than('525', '1111'))
print(larger_than('11', '0'))
print(larger_than('1', '1'))
