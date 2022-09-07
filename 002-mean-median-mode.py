from collections import defaultdict

dataset = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

mean = sum(dataset) / len(dataset)
print(f"Mean is: {mean}")

sorted_dataset = sorted(dataset)

if len(dataset) % 2 == 0:
    middle = len(sorted_dataset) // 2
    left_number = sorted_dataset[middle - 1]
    right_number = sorted_dataset[middle]
    total = (left_number + right_number) // 2
    print(f"Even number of elements median: {total}")
else:
    median = len(sorted_dataset) // 2
    print(f"Odd number of elements median: {sorted_dataset[median]}")


result = defaultdict(lambda: 1)
for num in dataset:
    result[num] += 1

print(f"Mode is: {[k for k in result if result[k] == max(result.values())][0]}")
