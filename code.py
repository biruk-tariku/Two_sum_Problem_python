def twosum(nums, target):
    length =len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]


n = [6, 4, 4, 3]
t = 10 

print(twosum(n, t))