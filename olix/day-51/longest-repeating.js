/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let i = 0;
  let j = 0;
  let max = 0;
  let map = new Map();
  while (j < s.length) {
    map.set(s[j], (map.get(s[j]) || 0) + 1);
    max = Math.max(max, map.get(s[j]));
    if (j - i + 1 - max > k) {
      map.set(s[i], map.get(s[i]) - 1);
      i++;
    }
    j++;
  }
  return j - i;
};

console.log(characterReplacement("ABAB", 2));
