function twoSum(nums: number[], target: number): number[] {
    let map = new Map();
    
    for(let i = 0; i < nums.length; i++) {
      let targetDiff = target - nums[i]
      if(map.has(targetDiff)) {
        return [map.get(target - nums[i]), i]
      }
      map.set(nums[i], i)
    }
  };