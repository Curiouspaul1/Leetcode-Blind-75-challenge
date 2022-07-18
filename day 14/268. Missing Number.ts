function missingNumber(nums: number[]): number {
  nums.sort((a, b) => a - b);

  if (nums[0] !== 0) return 0;
  if (nums.length === 1) return 1;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== nums[i + 1] - 1) {
      return nums[i] + 1;
    }
  }

  return nums.length;
}

