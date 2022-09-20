const substrings = (input) => {
  const strArr = input.split("");
  const checkArr = [];

  const isPalindrome = (str) => {
    if (str === str.split("").reverse().join("")) {
      console.log(str, "palindrome");
      !checkArr.includes(str) && checkArr.push(str);
    } else {
      console.log(str, "not palindrome");
    }
  };

  for (let j = 1; j <= strArr.length; j++) {
    let subs = "";
    for (let i = j; i <= strArr.length; i++) {
      let n = i - 1;
      subs = subs + strArr[n];
      isPalindrome(subs);
    }
  }

  console.log(checkArr.length);
};
substrings("ADOBECODEBANC");
