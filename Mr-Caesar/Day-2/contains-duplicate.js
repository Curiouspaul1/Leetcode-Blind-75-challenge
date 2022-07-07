/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
  hashSet = new Set(nums)
  
  return hashSet.size !== nums.length
  
};