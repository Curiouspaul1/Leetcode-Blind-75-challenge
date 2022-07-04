/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // create an indices array that will be returned
    // let indices = []
    //convert nums[] to a set for performance sake
    let numsSet = new Set(nums)
    for(let i = 0; i < nums.length; i++) {
        let xTarget = target - nums[i]
        if(numsSet.has(xTarget) && nums.indexOf(xTarget) !== i) {
            indices.push([i, nums.indexOf(xTarget)])
            break;
        } else {
            continue;
        }
    }
    return indices[0];
};
