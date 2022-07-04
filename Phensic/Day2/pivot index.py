from numpy import result_type


nums = [1,7,3,6,5,6] # 3
num1 = [1,2,3] # -1
num2 = [2,1,-1] # 0

# def function (nums):
#     total = sum(nums)
#     left = 0
#     result = 0
#     for i in nums:
#         left += i
#         for j in range(0, len(nums)): 
#             if (total - left - nums[j]) == left:
#                 result = j
#                 return result
#             elif (total - left - nums[j]) == 0:
#                 return 0
#             elif (total - left - nums[j]) == -1: 
#                 return -1
               
# print(function(num1))

for i, x in enumerate(nums):
    print(i, x)