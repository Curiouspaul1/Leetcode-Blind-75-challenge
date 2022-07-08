function maxSubArray(nums: number[]): number {
  if (nums.length == 0) {
    return 0;
  }
  if (nums.length == 1) {
    return nums[0];
  }
  let maxSubArray = nums[0];
  let currentSubArray = nums[0];
  for (let i = 1; i < nums.length; i++) {
    let num = nums[i];
    currentSubArray = Math.max(num, currentSubArray + num);
    maxSubArray = Math.max(maxSubArray, currentSubArray);
  }
  return maxSubArray;
}

console.assert(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6);
console.assert(maxSubArray([5, 4, -1, 7, 8]) == 23, "ss");
