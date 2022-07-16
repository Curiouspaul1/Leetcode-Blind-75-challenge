function countBits(n: number): number[] {
  let ans = [0];

  for (let i = 1; i <= n; i++) {
    ans.push(count(i));
  }
  return ans;
}

const count = (num: number): number => {
  let numberOfOnes = 0;

  while (num != 0) {
    num &= num - 1;
    numberOfOnes++;
  }

  return numberOfOnes;
};
