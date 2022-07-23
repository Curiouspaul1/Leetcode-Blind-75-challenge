function longestCommonSubsequence(s1: string, s2: string): number {
  if (s2.length < s1.length) {
    [s1, s2] = [s2, s1];
  }

  let previous = Array<number>(s1.length + 1).fill(0);
  let current = Array<number>(s1.length + 1).fill(0);

  for (let col = s2.length - 1; col > -1; col--) {
    for (let row = s1.length - 1; row > -1; row--) {
      if (s1[row] == s2[col]) {
        current[row] = 1 + previous[row + 1];
      } else {
        current[row] = Math.max(previous[row], current[row + 1]);
      }
    }
    [previous, current] = [current, previous];
  }

  return previous[0];
}
