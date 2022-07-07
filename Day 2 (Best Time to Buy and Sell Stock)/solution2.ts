// @ts-ignore

function maxProfit(prices: number[]): number {
  let max = 0;
  let minPrice = Infinity;
  for (const price of prices) {
    minPrice = Math.min(price, minPrice);
    max = Math.max(max, price - minPrice);
  }
  return max;
}
