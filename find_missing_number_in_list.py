# given a list of numbers 1 to n, one number is missing. Find the missing number

A = [1,2,3,4,6,7,8]

i = 0
while i < len(A):
    if A[i+1] == A[i] + 1:
        i = i +1 
    else:
        break
       
print(f"missing value in the list is : {A[i] + 1}")