function ashii(ar) {
  let arr = [];
  arr.sort();

  let minVal = arr.slice(0, 4).reduce((total, num) => total + num);
  let maxVal = arr.slice(1, 5).reduce((total, num) => total + num);

  console.log(minVal, maxVal);
}

function gate(time = "") {
  const stringLength = time.length;
  let timeArr = time.split("");
  const end = timeArr.splice(stringLength - 2, stringLength).join("");

  const start = timeArr.splice(0, 2).join("");

  let newStart = "";

  if (end === "AM") {
    if (start === "12") {
      newStart = "00";
    } else {
      newStart = start;
    }
  } else if (end === "PM") {
    if (start === "12") {
      newStart = start;
    } else {
      newStart = String(Number(start) + 12);
    }
  }

  const final = newStart + timeArr.join("");
  console.log(final);
}
gate("01:00:00PM");
