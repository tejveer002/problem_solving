def removeElement(nums, val):
    count = 0
    left = 0
    right = len(nums)-1 
    while left <= right:
        if nums[left] == val and nums[right] == val:
            right -= 1
        elif nums[left] == val and nums[right] != val:
            count += 1
            nums[left] = nums[left] ^ nums[right]
            nums[right] = nums[left] ^ nums[right]
            nums[left] = nums[left] ^ nums[right]
            right -= 1
            left += 1
        elif nums[left] != val and nums[right] == val:
            right -= 1
        elif nums[left] != val and nums[right] != val:
            left += 1
            count += 1
    return count, nums
        
nums = [3,2,2,3]
val = 3
res = removeElement(nums, val)
print(res)