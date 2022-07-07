function productExceptSelf(nums: number[]): number[] {
  const result = new Array<number>(nums.length);
  let post = 1;
  result[0] = 1;
  for (let i = 0; i < nums.length - 1; i++) {
    result[i + 1] = nums[i] * result[i];
  }
  for (let i = nums.length - 1; i > 0; i--) {
    post *= nums[i];
    result[i - 1] *= post;
  }
  console.log(result);
  return result;
}

console.assert(JSON.stringify(productExceptSelf([1, 2, 3, 4])) == JSON.stringify([24, 12, 8, 6]));
console.assert(JSON.stringify(productExceptSelf([1, 2, 3, 4, 5])) == JSON.stringify([120, 60, 40, 30, 24]));
console.assert(JSON.stringify(productExceptSelf([-1, 1, 0, -3, 3])) == JSON.stringify([0, 0, 9, 0, 0]));
