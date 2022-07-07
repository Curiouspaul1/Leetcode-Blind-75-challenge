// @ts-ignore
function twoSum(nums: number[], target: number): number[] {
  for (let num = 0; num < nums.length; num++) {
    for (let i = num; i < nums.length; i++) {
      if (nums[num] + nums[i] == target) return [num, i];
    }
  }
  return [];
}
