# reverse a list without creating a new list

list = [1,2,3,4,5,6,7]

i = len(list) - 1
while i>=0:
    list.append(list[i])
    list.pop(i)
    i = i-1

print(list)

