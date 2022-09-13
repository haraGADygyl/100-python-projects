def merge(list1, list2):
    new_list = []
    a = 0
    b = 0

    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            new_list.append(list1[a])
            a += 1
        else:
            new_list.append(list2[b])
            b += 1

    while a < len(list1):
        new_list.append(list1[a])
        a +=1

    while b < len(list2):
        new_list.append(list2[b])
        b += 1

    return new_list


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        mid = len(unsorted_list) // 2
        left = merge_sort(unsorted_list[:mid])
        right = merge_sort(unsorted_list[mid:])

        new_list = merge(left, right)

        return new_list


numbers = [56, 89, 45, 34, 90, 32, 20, 67, 43]
print(merge_sort(numbers))
