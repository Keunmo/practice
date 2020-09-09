length = int(input())
nums = []
tmp = length
while tmp:
    nums.append(int(input()))
    tmp -= 1
mini = 0
inclist = []
for i in range(length):
    mini = nums[i]
    inc = [mini]
    for j in nums[i:]:
        if j > mini:
            mini = j
            inc.append(mini)
    inclist.append(inc)
maxl = 0
# print(inclist)
for i in inclist:
    if len(i) > maxl:
        maxl = len(i)
print(maxl)
# # return maxl

# 3 1 2 3 4 1 5 1 6 4

# 1 2 3 4 5 6