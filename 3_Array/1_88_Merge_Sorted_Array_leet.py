def merge(nums1, m, nums2, n):
	while m > 0 and n > 0:
		if nums1[m - 1] >= nums2[n - 1]:
			nums1[m + n - 1] = nums1[m - 1]
			m -= 1
		else:
			nums1[m + n - 1] = nums2[n - 1]
			n -= 1
	for i in range(0, n):
		nums1[i] = nums2[i]
	return nums1


nums1 = [0,0,3,0,0,0,0,0,0]
m = 3
nums2 = [-1,1,1,1,2,3]
n = 6
res = merge(nums1, m, nums2, n)
print(res)

# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3


#"""    Do not return anything, modify nums1 in-place instead. """
#     count1 = m
#     count2 = n
#     count = False
#     i = 0 
#     j = 0 

#     if m == 0 and n != 0:
#         nums1 = nums2
#         return nums1

#     elif n == 0:
#         return nums1
    
#     while i <= count1 + count2 -1 and j <= count2-1:
#         if nums1[i] > nums2[j]:
#             for k in range(m+n-1,i-1,-1):
#                 nums1[k] = nums1[k-1]
#             nums1[i] = nums2[j]
#             i += 1
#             j += 1
#             count = True
#             # count1 += 1
#             print(1)
        
#         elif nums1[i] < nums2[j] and i >= count1-1 and j <= count2-1 and nums1[i] == 0 and count == True:
#             nums1[i] = nums2[j]
#             i += 1
#             j += 1
#             print(4)

#         elif nums1[i] < nums2[j]:
#             i += 1
#             print(2)
#         elif nums1[i] == nums2[j]:
#             i += 1
#             print(3)
        
#         print(f"i-->{i}, j-->{j}, nums1 --> {nums1}")
        
#     # if nums1[-1] < nums2[-1]:

    
#     return nums1
# # and i >= count1-1 and j < count2