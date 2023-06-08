// 2512 예
//https://www.acmicpc.net/problem/2512

let [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");
// const [N, ...input] = require("fs")
//   .readFileSync("./text.txt")
//   .toString()
//   .split("\n");

const M = +input.pop();
const moneys = input[0].split(" ").map((v) => +v);

const moneySums = (moneys, maximums) =>
  moneys.reduce((pv, cv) => (cv > maximums ? maximums + pv : pv + cv), 0);

const fl = Math.floor;
const top = Math.max(...moneys);
let jumpNum = fl(top / 2);
const minValues = [0];

const solve = (key, isPlus) => {
  if (jumpNum <= 0) return;
  const maximums = isPlus ? key + jumpNum : key - jumpNum;
  const sumValues = moneySums(moneys, maximums);

  if (sumValues < M) {
    if (!isPlus) jumpNum = fl(jumpNum / 2);
    minValues.push(maximums);
    solve(maximums, true);
  } else {
    if (isPlus) jumpNum = fl(jumpNum / 2);
    solve(maximums, false);
  }
};
if (moneySums(moneys, top) < M) minValues.push(top);
else solve(0, true);
console.log(Math.max(...minValues));
