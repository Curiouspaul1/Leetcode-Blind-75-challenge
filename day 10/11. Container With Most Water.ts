function maxArea(nums: number[]): number {
  let left = 0;
  let right = nums.length - 1;
  let maxArea = 0;

  while (left < right) {
    let height = Math.min(nums[left], nums[right]);
    let width = Math.abs(right - left);
    maxArea = Math.max(maxArea, height * width);

    if (nums[right] > nums[left]) {
      left++;
    } else if (nums[left] > nums[right]) {
      right--;
    } else {
      right--;
      left++;
    }
  }

  return maxArea;
}
