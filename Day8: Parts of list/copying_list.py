# Copy this list and multiple values by 2
# and print the original list and copied list
nums = [1, 2, 4, 5, 6, 6, 7, 3]
second = nums[:]

for i in range(len(second)):
    second[i] = second[i] * 2
    
print(nums)
print(second)
