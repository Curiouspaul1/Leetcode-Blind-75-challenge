function maxSubArray(nums: number[]): number {
  let maxSum = nums[0];
  let sum = 0;

  for (const num of nums) {
    if (sum < 0) {
      sum = 0;
    }
    sum += num;
    maxSum = Math.max(maxSum, sum);
  }

  return maxSum;
}
