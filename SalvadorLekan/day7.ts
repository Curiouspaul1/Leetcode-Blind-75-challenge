function findMin(nums: number[]): number {
  if (nums.length === 1) {
    return nums[0];
  }
  if (nums[0] < nums[nums.length - 1]) {
    return nums[0];
  }
  let ma = nums.length - 1;
  let mi = 0;
  while (true) {
    let currentIndex = Math.round((mi + ma) / 2);
    if (nums[currentIndex] > nums[currentIndex + 1]) {
      return nums[currentIndex + 1];
    }
    if (nums[currentIndex] < nums[currentIndex - 1]) {
      return nums[currentIndex];
    }
    if (nums[currentIndex] < nums[0]) {
      ma = currentIndex;
    } else mi = currentIndex;
  }
}

console.assert(findMin([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) === 0, "0");
console.assert(findMin([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) === 0, "1");
console.assert(findMin([2, 3, 4, 5, 6, 7, 8, 9, 0, 1]) === 0, "2");
console.assert(findMin([3, 4, 5, 6, 7, 8, 9, 0, 1, 2]) === 0, "3");
console.assert(findMin([4, 5, 6, 7, 8, 9, 0, 1, 2, 3]) === 0, "4");
console.assert(findMin([5, 6, 7, 8, 9, 0, 1, 2, 3, 4]) === 0, "5");
console.assert(findMin([6, 7, 8, 9, 0, 1, 2, 3, 4, 5]) === 0, "6");
console.assert(findMin([7, 8, 9, 0, 1, 2, 3, 4, 5, 6]) === 0, "7");
console.assert(findMin([8, 9, 0, 1, 2, 3, 4, 5, 6, 7]) === 0, "8");
console.assert(findMin([9, 0, 1, 2, 3, 4, 5, 6, 7, 8]) === 0, "9");
