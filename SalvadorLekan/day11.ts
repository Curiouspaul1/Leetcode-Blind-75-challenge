function getSum(n: number, m: number): number {
  if (!n) return m;
  if (!m) return n;
  while (m) {
    let temp = (n & m) << 1;
    n ^= m;
    m = temp;
  }
  return n;
}

console.log(getSum(3, 5));
console.log(getSum(3, 6));
console.log(getSum(3, 7));
console.log(getSum(3, 8));
