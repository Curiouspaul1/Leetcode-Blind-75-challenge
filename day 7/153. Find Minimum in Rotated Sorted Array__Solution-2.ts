function findMin(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;
  let midIndex = 0;

  if (nums.length === 1) return nums[0];

  if (nums[right] > nums[0]) return nums[0];

  while (right >= left) {
    midIndex = Math.floor((right + left) / 2);

    if (nums[midIndex] > nums[midIndex + 1]) return nums[midIndex + 1];

    if (nums[midIndex - 1] > nums[midIndex]) return nums[midIndex];

    if (nums[midIndex] > nums[0]) {
      left = midIndex + 1;
    } else {
      right = midIndex - 1;
    }
  }
}
