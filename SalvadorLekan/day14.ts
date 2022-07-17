function missingNumber(nums: number[]): number {
  let i = 0;
  let sum = 0;
  let actualsum = 0;
  while (i < nums.length) {
    sum += i + 1;
    actualsum += nums[i];
    i++;
  }
  return sum - actualsum;
}
console.log(missingNumber([3, 0, 1]));
