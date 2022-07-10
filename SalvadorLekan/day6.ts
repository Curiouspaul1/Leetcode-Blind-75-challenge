function maxProduct(nums: number[]): number {
  if (nums.length === 1) {
    return nums[0];
  }
  let max = -Infinity;
  let currentMax = 1;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      currentMax = 1;
      max = Math.max(max, 0);
    } else {
      currentMax *= nums[i];
      max = Math.max(currentMax, max);
    }
  }

  currentMax = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    if (nums[i] === 0) {
      currentMax = 1;
      max = Math.max(max, 0);
    } else {
      currentMax *= nums[i];
      max = Math.max(currentMax, max);
    }
  }

  return max;
}

console.assert(maxProduct([2, 3, -2, 4]) === 6);
console.assert(maxProduct([-2, 0, -1]) === 0);
console.assert(maxProduct([-2, 3, -4]) === 24);
console.assert(maxProduct([-2, 3, -4, -5]) === 60);
console.assert(maxProduct([-20, 3, -4, -5]) === 240);
console.assert(maxProduct([-2, 3, -4, -5, -6]) === 720);
console.assert(maxProduct([0, 2]) === 2);
console.assert(maxProduct([-3, -1, 3, 5, -6, -6, -1, 6, -3, -5, 1, 0, -6, -5, 0, -2, 6, 1, 0, 5]) === 48600);
