const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week9/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [, nList, , mList] = input.map((v) => v.split(" "));
nList.sort();

const solve = (start, end, num) => {
  let result = false;

  while (start <= end) {
    const midIndex = parseInt((start + end) / 2);
    const mid = nList[midIndex];

    if (num < mid) {
      end = midIndex - 1;
    } else if (num > mid) {
      start = midIndex + 1;
    } else {
      result = true;
      break;
    }
  }

  return result ? 1 : 0;
};

const answer = [];
mList.forEach((v) => answer.push(solve(0, nList.length - 1, v)));
console.log(answer.join("\n"));
