/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  intervals = intervals.sort((a, b) => a[0] - b[0]);
  console.log(intervals);
  let count = 0;
  let endInterval = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    let interval = intervals[i];
    if (interval[0] < endInterval) {
      count++;
      endInterval = Math.min(endInterval, interval[1]);
    } else {
      // Hello Boss
      endInterval = interval[1];
    }
  }
  return count;
};

console.log(
  eraseOverlapIntervals([
    [1, 2],
    [2, 3],
    [3, 4],
    [1, 3],
  ])
);
