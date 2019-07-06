# replace item at the given index with -1, and finally -1 should be last element

list = [1,2,3,4,5]

index = 3
for i in range(len(list)):
    if i == index:
        list[index] = -1

print(list)

for j in range(len(list)):
    if list[j] == -1:
        a = list[j]
        b = list[j+1]
        list[j] = b
        list[j+1] = a
        if list[-1] == -1:
            break
    else:
        continue
        

print(list)


