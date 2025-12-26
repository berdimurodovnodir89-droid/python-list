nums = [3, 5, 3, 5, 5, 2, 5, 5, 1, 1, 1, 1]
max_num = nums[0]
for num in nums :
    if nums.count(num) > nums.count(max_num):
        max_num = num

print(max_num)