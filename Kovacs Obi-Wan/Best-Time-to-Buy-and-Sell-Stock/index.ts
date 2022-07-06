function maxProfit(prices: number[]): number {
    let profit = 0;
    let buy = 0;
    let sell = 1;

    while (sell < prices.length) {
        if (prices[buy] < prices[sell]) {
            profit = Math.max(profit, prices[sell] - prices[buy])
        } else {
            buy = sell
        }
        sell += 1
    }
    return profit
};