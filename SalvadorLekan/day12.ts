function hammingWeight(n: number): number {
  let count = 0b0;
  while (n) {
    n &= n - 1;
    count += 0b1;
  }
  return count;
}
