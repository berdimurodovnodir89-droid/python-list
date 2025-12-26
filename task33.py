list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7]

filtr = []

for list in list1:
    if list in list2 and list not in  filtr:
        filtr.append(list)

print(filtr)