// @ts-ignore
function twoSum(nums: number[], target: number): number[] {
  const map = {} as { [key: number]: number };
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    const index = map[diff];
    if (index !== undefined) {
      return [index, i];
    }
    map[nums[i]] = i;
  }
  return [];
}

twoSum([2, 7, 11, 15], 9);
