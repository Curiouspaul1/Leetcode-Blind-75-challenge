function productExceptSelf(nums: number[]): number[] {
  const leftArray = new Array(nums.length);
  const rightArray = new Array(nums.length);
  leftArray[0] = 1;
  rightArray[nums.length - 1] = 1;
  for (let i = 1; i < nums.length; i++) {
    leftArray[i] = leftArray[i - 1] * nums[i - 1];
  }
  for (let i = nums.length - 2; i >= 0; i--) {
    rightArray[i] = rightArray[i + 1] * nums[i + 1];
  }
  return nums.map((num, index) => leftArray[index] * rightArray[index]);
}
