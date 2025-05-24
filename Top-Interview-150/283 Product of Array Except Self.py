prefix = [1] * (len(nums))
suffix = [1] * (len(nums))
n = len(nums)

for i in range(1, len(nums)):
    j =n-i-1
    prefix[i] = prefix[i-1] * nums[i - 1]
    suffix[j] = suffix[j +1] * nums[j+1]
    
for i in range(len(prefix)):
    prefix[i] *=suffix[i]

