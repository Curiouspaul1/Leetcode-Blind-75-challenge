function reverseBits(n: number): number {
  if (n === 0) return 0;
  let length = 32;
  let i = 1;
  let res = 0;
  while (i <= 32) {
    res = res | ((n << (length - 1)) >>> (i - 1));
    n = n >>> 1;
    i++;
  }
  return res >>> 0;
}
