/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  let result = "";
  let map = new Map();
  for (let i = 0; i < t.length; i++) {
    if (map.has(t[i])) map.set(t[i], map.get(t[i]) + 1);
    else map.set(t[i], 1);
  }
  let count = map.size;
  let left = 0;
  let right = 0;
  while (right < s.length) {
    let c = s[right];
    if (map.has(c)) {
      map.set(c, map.get(c) - 1);
      if (map.get(c) === 0) count--;
    }
    right++;
    while (count === 0) {
      let temp = s.substring(left, right);
      if (result === "" || temp.length < result.length) result = temp;
      let c = s[left];
      if (map.has(c)) {
        map.set(c, map.get(c) + 1);
        if (map.get(c) > 0) count++;
      }
      left++;
    }
  }
  return result;
};

console.log(minWindow("ADOBECODEBANC", "ABC"));
