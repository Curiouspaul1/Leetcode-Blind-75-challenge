function lengthOfLIS(nums: number[]): number {
  if (nums.length < 2) return nums.length;
  let max = 1;
  const dp = new Array(nums.length).fill(1);
  for (let i = nums.length - 2; i > -1; i--) {
    const curr = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      const next = nums[j];
      if (curr < next) dp[i] = Math.max(dp[i], 1 + dp[j]);
      if (dp[i] > max) max = dp[i];
    }
  }
  return max;
}

// console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]));
console.log(lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]));
