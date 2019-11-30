my_list = []

for i in range((10)):
    my_list.append(i)


def linear_search(list, item):
    for i, x in enumerate(list):
        guess = x
        if guess == item:
            return i


print(linear_search(my_list, 3))
