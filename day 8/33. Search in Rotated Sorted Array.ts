function search(nums: number[], target: number): number {
  let left = 0;
  let right = nums.length - 1;
  let midIndex = 0;
  
  if (nums[0] === target) return 0;
    
  while(left <= right) {
    midIndex = Math.floor((right + left) / 2);
    
    if(nums[midIndex] === target) return midIndex
    
    if(nums[midIndex] >= nums[left]) {
      if((target > nums[midIndex]) || (target  < nums[left])) {
        left = midIndex + 1
      } else {
        right = midIndex - 1
      }
    } else {
      if((target < nums[midIndex]) || (target > nums[right])) {
        right = midIndex - 1
      } else {
        left = midIndex + 1
      }
    }
  }
  
  return -1
};