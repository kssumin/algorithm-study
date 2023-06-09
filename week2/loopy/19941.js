// 19941 햄버거 분배
// https://www.acmicpc.net/problem/19941

let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const input = require("fs")
//   .readFileSync("./text.txt")
//   .toString()
//   .trim()
//   .split("\n");

const [N, K] = input[0].split(" ").map(Number);
const board = input[1].split("");

const canEat = (h) => {
  for (let i = Math.max(h - K, 0); i <= Math.min(h + K, N); i++) {
    if (board[i] == "H") {
      board[i] = "E";
      return i;
    }
  }
  return -1;
};

let count = 0;
const solve = () => {
  for (let i = 0; i < N; i++) if (board[i] == "P" && canEat(i) + 1) count += 1;
};

solve();
console.log(count);
