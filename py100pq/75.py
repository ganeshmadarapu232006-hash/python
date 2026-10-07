list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for i in list1:
    if i not in list2:
        result.append(i)

print(result)