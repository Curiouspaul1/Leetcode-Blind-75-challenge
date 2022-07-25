global maximum
def _lis(arr, n):

	global maximum

	if n == 1:
    print('Entered base case n==1')
    return 1
   
	maxEndingHere = 1

	for i in range(1, n):
	  print("for {} in {}".format(i, list(rang(1,n))))
		res = _lis(arr, i)
		print('lis(arr, {})'.format(i))
		print("if arr[{}-1] < arr[{}-1] and {}+1 > {}:".format(i,n,res,maxEndingHere))
		if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
		  print('Yes it is')
			maxEndingHere = res + 1
			print("maxEndingHere = {} + 1".format(res))

  print(maximum = max("maximum = max({}, {})".format(maximum,maxEndingHere))
	maximum = max(maximum, maxEndingHere)
	print("Value of maximum: {}".format(maximum))

  print("Returning maxEndingHere: {}".format(maxEndingHere))
	return maxEndingHere


def lis(arr):
	global maximum

	n = len(arr)

	maximum = 1
	print("Initializing maximum as 1")

	_lis(arr, n)

	return maximum

arr = [4,-2,3,-4,8]
n = len(arr)
print ("Length of lis is ", lis(arr))

