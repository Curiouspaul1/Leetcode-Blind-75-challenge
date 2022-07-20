function climbStairs(n: number): number {
  let i = 1;
  let j = 1;
  while (n !== 1) {
    i += j;
    j = i - j;
    n--;
  }
  return i;
}
