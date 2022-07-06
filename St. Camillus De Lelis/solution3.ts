// @ts-ignore
function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>();
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    const index = map.get(diff);
    if (index !== undefined) {
      return [index, i];
    }
    map.set(nums[i], i);
  }
}
console.log(twoSum([2, 7, 11, 15], 9));
