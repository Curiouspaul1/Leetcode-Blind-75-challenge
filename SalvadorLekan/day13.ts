function countBits(n: number): number[] {
  const result: number[] = new Array(n + 1);
  let i = 0;

  while (i <= n) {
    result[i] = hammingWeight(i);
    i++;
  }

  return result;
}
// @ts-ignore
function hammingWeight(n: number): number {
  let count = 0b0;
  while (n) {
    n &= n - 1;
    count += 0b1;
  }
  return count;
}
console.log(countBits(5));
console.log(countBits(2));
// countBits(5);
