// @ts-ignore
function maxProfit(prices: number[]): number {
  let maxPrice = 0;
  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      const diff = prices[j] - prices[i];
      if (diff > maxPrice) {
        maxPrice = diff;
      }
    }
  }
  return maxPrice;
}

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
