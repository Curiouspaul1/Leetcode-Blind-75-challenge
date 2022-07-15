function hammingWeight(n: number): number {
  let sum = 0;

  while (n) {
    sum += n % 2;
    n = n >>> 1;
  }

  return sum;
}
