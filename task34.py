num = [1, 2, 3, 7, 8, 9]

result = []

for i in range(len(num)):
    for j in  range(i + 1 , len(num)):
      if num[i] + num[j] == 10:
         result.append([num[i], num[j]])

print(result)