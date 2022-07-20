function climbStairs(n: number, mapMemo = new Map<number, number>()): number {
  if (n === 1) return 1;

  if (n === 2) return 2;

  if (!mapMemo.has(n)) {
    mapMemo.set(n, climbStairs(n - 1, mapMemo) + climbStairs(n - 2, mapMemo));
  }

  return mapMemo.get(n) as number;
}
