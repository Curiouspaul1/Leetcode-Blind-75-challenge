/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === "(" || s[i] === "{" || s[i] === "[") stack.push(s[i]);
    else {
      if (stack.length === 0) return false;
      let c = stack.pop();
      if (s[i] === ")" && c !== "(") return false;
      if (s[i] === "}" && c !== "{") return false;
      if (s[i] === "]" && c !== "[") return false;
    }
  }
  return stack.length === 0;
};
