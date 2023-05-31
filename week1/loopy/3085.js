// 3085 사탕게임
// https://www.acmicpc.net/problem/3085

//const [N, ...input] = require("fs")
//  .readFileSync("/dev/stdin")
//  .toString()
//  .split("\n");
const [N, ...input] = require("fs")
  .readFileSync("./text.txt")
  .toString()
  .trim()
  .split("\n");

const board = input.map((v) => v.split(""));
const m = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

const switchBoard = (x1, y1, x2, y2) => {
  const temp = board[x1][y1];
  board[x1][y1] = board[x2][y2];
  board[x2][y2] = temp;
  return temp;
};

const isOverBoard = (x, y) => x >= N || y >= N || x <= -1 || y <= -1;

let result = [];
const check = (x, y, next) => {
  if (isOverBoard(x, y)) return 0;

  let key = board[x][y];
  let count = 0;
  while (!isOverBoard(x, y)) {
    if (key != board[x][y]) {
      return count;
    }
    count++;
    [x, y] = next(x, y);
  }
  return count;
};

for (let i = 0; i < board.length; i++) {
  for (let j = 0; j < board[i].length; j++) {
    for (let k = 0; k < 4; k++) {
      if (isOverBoard(i + m[k][0], j + m[k][1])) continue;
      switchBoard(i, j, i + m[k][0], j + m[k][1]);
      result.push(
        Math.min(
          ...Array(4).map((i) => {
            check(i, j, (i, j) => [i + m[k][0], j + m[k][0]]);
          })
        )
      );
      switchBoard(i + m[k][0], j + m[k][1], i, j);
    }
  }
}

console.log(Math.min(...result));
