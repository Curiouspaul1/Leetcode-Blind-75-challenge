function maxProduct(nums: number[]): number {
  let result = Math.max(...nums);
  let currMin = 1;
  let currMax = 1;

  for (const num of nums) {
    let tmp = num * currMax;
    currMax = Math.max(num * currMax, num * currMin, num);
    currMin = Math.min(tmp, num * currMin, num);

    result = Math.max(result, currMax, currMin);
  }

  return result;
}
