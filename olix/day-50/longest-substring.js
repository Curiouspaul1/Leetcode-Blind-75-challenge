/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let i = 0;
  let j = 0;
  let max = 0;
  let set = new Set();
  while (j < s.length) {
    if (!set.has(s[j])) {
      set.add(s[j]);
      j++;
      max = Math.max(max, set.size);
    } else {
      set.delete(s[i]);
      i++;
    }
  }
  return max;
};

console.log(lengthOfLongestSubstring("abcabcbb"));
