function containsDuplicate(nums: number[]): boolean {
  let isDuplicate = false;
  const mySet = new Set<number>();
  for (const num of nums) {
    if (mySet.has(num)) {
      isDuplicate = true;
      break;
    }
    mySet.add(num);
  }
  return isDuplicate;
}
console.log(containsDuplicate([1, 2, 3, 4]));
