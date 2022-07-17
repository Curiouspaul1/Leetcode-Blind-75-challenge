/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  const totalLength = nums.length
  const sumOfN = Math.floor((totalLength * (totalLength + 1)) / 2)

  const sumOfInput = nums.reduce((x, y) => x + y, 0)

  return sumOfN - sumOfInput
}
