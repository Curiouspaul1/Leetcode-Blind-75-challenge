/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
  hashMap = {}
  
  for(let j=0 ; j < nums.length; j++) {
    hashMap[nums[j]] = j
  }   
  
  for(let k=0; k < nums.length; k++) {
    if(nums[k] === target) {
        return hashMap[nums[k]]
    }   
  }
  return -1
}