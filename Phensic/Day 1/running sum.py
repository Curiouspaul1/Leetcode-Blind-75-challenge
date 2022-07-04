nums1  = [1,2,3,4]

def runningSum(num):
    arr_len = len(num)
    # nums = []
    for i in range (1, arr_len):
        num[i]+= num[i - 1] 
        print(num)



runningSum(nums1)
