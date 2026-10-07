list1 = [1, 2, 3, 4]
list2 = [2, 3, 4, 5]
list3 = [3, 4, 6]

result = []

for i in list1:
    if i in list2 and i in list3:
        result.append(i)

print(result)