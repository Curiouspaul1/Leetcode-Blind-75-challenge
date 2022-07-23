/**
* @ param {number[]} nums
* @ return {number}
*/
var lengthOfLIS = function(nums) {
    if(nums.length < 2) return nums.length
    let max = 1
    const arr = new Array(nums.length).fill(1)
    for (let i = nums.length - 1; i > -1; i--) {
        for (let j = i + 1; j < nums.length; j++) {
            if(nums[i] < nums[j]) {
                arr[i] = Math.max(arr[i], 1 + arr[j])
            }
            if(arr[i] > max) {
                max = arr[i]
            }
        }
    }
    return max
}
