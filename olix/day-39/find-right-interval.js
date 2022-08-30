/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var findRightInterval = function (intervals) {
  let result = [];
  let sorted = intervals.sort((a, b) => a[0] - b[0]);
  for (let i = 0; i < intervals.length; i++) {
    let start = intervals[i][0];
    let end = intervals[i][1];
    let index = binarySearch(sorted, end);
    result.push(index);
  }
  return result;
};

function binarySearch(arr, target) {
  let start = 0;
  let end = arr.length - 1;
  while (start <= end) {
    let mid = Math.floor((start + end) / 2);
    console.log(mid);
    if (arr[mid][0] === target) {
      return mid;
    } else if (arr[mid][0] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }
  return -1;
}

console.log(
  binarySearch([
    [1, 4],
    [2, 3],
    [3, 4],
  ])
);
