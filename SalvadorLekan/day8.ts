function search(nums: number[], target: number): number {
  let l = 0,
    r = nums.length - 1;
  while (l <= r) {
    let mid = Math.floor((l + r) / 2);
    if (nums[mid] === target) return mid;

    if (nums[l] <= nums[mid]) {
      if (target < nums[l] || target > nums[mid]) l = mid + 1;
      else r = mid - 1;
    } else {
      if (target < nums[mid] || target > nums[r]) r = mid - 1;
      else l = mid + 1;
    }
  }
  return -1;
}

console.assert(search([3, 1], 1) === 1, `9`);
console.assert(search([1, 3], 1) === 0, `0`);
console.assert(search([4, 5, 6, 7, 0, 1, 2], 0) === 4, `8`);

console.assert(search([4, 5, 6, 7, 8, 9, 0, 1, 2, 3], 7) === 3, `3`);
console.assert(search([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], 7) === 1, `1`);
console.assert(search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7) === 7, `7`);
console.assert(search([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 7) === 6, "6");
console.assert(search([2, 3, 4, 5, 6, 7, 8, 9, 0, 1], 7) === 5, `5`);
console.assert(search([3, 4, 5, 6, 7, 8, 9, 0, 1, 2], 7) === 4, `4`);
console.assert(search([5, 6, 7, 8, 9, 0, 1, 2, 3, 4], 7) === 2, `2`);
console.assert(search([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], 7) === 0, `0`);
