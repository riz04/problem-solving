x = [1,2,3,4,5,8,7]

max = max(x)
print(max)

for i in range(max+1):
      if i == 0:
          print("go ahead")
      else:
          if i not in x:
              break
    
print(f"Missing number is {i}")