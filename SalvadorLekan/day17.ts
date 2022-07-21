function coinChange(coins: number[], amount: number): number {
  const dp = new Array<number>(++amount);
  dp[0] = 0;
  coins.sort((a, b) => a - b);
  for (let i = 1; i < amount; i++) {
    dp[i] = Number.MAX_SAFE_INTEGER;
    for (let c of coins) {
      if (i - c < 0) break;
      if (dp[i - c] != Number.MAX_SAFE_INTEGER) dp[i] = Math.min(dp[i], 1 + dp[i - c]);
    }
  }
  return dp[--amount] == Number.MAX_SAFE_INTEGER ? -1 : dp[amount];
}

// console.log(coinChange([1, 2, 5], 11));
// console.log(coinChange([2, 5, 10, 1], 27));
// console.log(coinChange([1, 2, 5], 0));
// console.log(coinChange([1, 2, 5], 1));
// console.log(coinChange([1, 2, 5], 2));
// console.log(coinChange([1, 2, 5], 3));
console.log(coinChange([186, 419, 83, 408], 6249));

// @ts-ignore
// console.log(Math.min(2, undefined));
