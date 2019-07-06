x = [1,2,3,4,5,8,7]

max = max(x)

sum = 0
for i in x:
    sum = sum + i

missing_number = int(((max)*(max + 1))/2 - sum)
print(missing_number)
