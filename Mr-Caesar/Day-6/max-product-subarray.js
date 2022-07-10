/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxProduct = function(nums) {
  let maxP = nums[0]
  let minP = nums[0]
  let res = nums[0]
  
  for(let j=1; j < nums.length; j++) {
      
      let x = Math.max(nums[j] * maxP, nums[j] * minP, nums[j])
      let y = Math.min(maxP * nums[j], nums[j] * minP, nums[j])    
      maxP = x
      minP = y        
      res = Math.max(res, maxP)            
  }
  return res
};