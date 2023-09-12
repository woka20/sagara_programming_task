def maxProductOfThree(nums):
    nums.sort()
    
    product1 = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1]
    
    return max(product1, product2)



print("Test Case 1 : ", maxProductOfThree([1,2,3]))
print("Test Case 2 : ", maxProductOfThree([-10,-10,1,2,3]))

