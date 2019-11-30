import bisect
my_list = []

for i in range((10)):
    my_list.append(i)

print(my_list)
print(bisect.bisect_left(my_list, 3))
