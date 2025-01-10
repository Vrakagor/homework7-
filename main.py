my_list = [0, 1, 0, 12, 3]
result = []
for x in my_list:
    if x != 0:
        result.append(x)
for x in my_list:
    if x == 0:
        result.append(x)
print(result)
