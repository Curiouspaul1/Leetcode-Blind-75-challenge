function maxArea(height: number[]): number {
  let maxArea = 0;
  let l = 0;
  let r = height.length - 1;
  while (l < r) {
    let left = height[l];
    let right = height[r];
    let min = Math.min(left, right);
    maxArea = Math.max(maxArea, min * (r - l));
    if (right === min) r--;
    else l++;
  }
  return maxArea;
}

console.assert(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) === 49);
// console.assert(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7, 9]) === 49);
// console.assert(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7, 9, 10]) === 49);
