// 2512 예산 solve
//https://www.acmicpc.net/problem/2512

let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs")
//   .readFileSync("./text.txt")
//   .toString()
// .trim()
//   .split("\n");
const [N, moneys, M] = [+input[0], input[1].split(" ").map(Number), +input[2]];

let bottom = 0;
let top = Math.max(...moneys);

const moneySums = (moneys, maximums) =>
  moneys.reduce((pv, cv) => (cv > maximums ? maximums + pv : pv + cv), 0);

let result = 0;

while (bottom <= top) {
  let mid = Math.floor((bottom + top) / 2);

  if (moneySums(moneys, mid) <= M) {
    if (mid > result) result = mid;
    bottom = mid + 1;
  } else {
    top = mid - 1;
  }
}

console.log(result);
