/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
let intervalIntersection = function (firstList, secondList) {
  let result = [];
  let i = 0;
  j = 0;

  while (i < firstList.length && j < secondList.length) {
    let first = firstList[i];
    let second = secondList[j];
    if (first[1] < second[0]) {
      i++;
    } else if (second[1] < first[0]) {
      j++;
    } else {
      result.push([
        Math.max(first[0], second[0]),
        Math.min(first[1], second[1]),
      ]);
      if (first[1] < second[1]) {
        i++;
      } else {
        j++;
      }
    }
  }
  return result;
};
