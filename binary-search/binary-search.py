my_list = []

for i in range((10)):
    my_list.append(i)


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            low = mid + 1
        else:
            high = mid - 1

    return None


print(binary_search(my_list, 3))
