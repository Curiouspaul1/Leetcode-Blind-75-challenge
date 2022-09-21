/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  let map = new Map();
  for (let i = 0; i < strs.length; i++) {
    let key = strs[i].split("").sort().join("");
    if (map.has(key)) map.get(key).push(strs[i]);
    else map.set(key, [strs[i]]);
  }
  return [...map.values()];
};
