# def find_duplicates(arr):
#     duplicates = set()
#
#     for i in arr:
#         if arr.count(i) > 1:
#             print(f"Duplicate found {i}")
#             duplicates.add(i)
#
#     return duplicates
#
#
# data = ['a', 'b', 'c', 'd', 'a', 'c']
# data2 = range(1_000_000)
# data3 = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8]
# names = ["Aman", "Akanksha", "Divyansha", "Devyansh",
#          "Aman", "Diksha", "Akanksha"]
#
# print(find_duplicates(data3))


def find_duplicates(x):
    length = len(x)
    duplicates = []
    for i in range(length):
        n = i + 1
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:
                duplicates.append(x[i])
    return duplicates


names = ["Aman", "Akanksha", "Divyansha", "Devyansh",
         "Aman", "Diksha", "Akanksha", "Aman"]

print(find_duplicates(names))
