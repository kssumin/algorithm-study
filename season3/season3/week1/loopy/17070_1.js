// 17070 파이프 옮기기 1
// https://www.acmicpc.net/problem/17070

const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const [N, ...input] = require("fs")
//   .readFileSync("./text.txt")
//   .toString()
//   .trim()
//   .split("\n");

const board = input.map((v) => v.split(" "));

const moveList = [
  [1, 0],
  [1, 1],
  [0, 1],
];

const canMoveList = [
  [0, 1],
  [0, 1, 2],
  [1, 2],
];

const whenMoveCheckList = [
  [[1, 0]],
  [
    [1, 0],
    [1, 1],
    [0, 1],
  ],
  [[0, 1]],
];

let goIndex = 0; // 0: 우측, 1: 대각선, 2: 하단

// 초기화
let x = 1;
let y = 0;

const canMove = (checkIndex) =>
  canMoveList[checkIndex].map((c) =>
    whenMoveCheckList[c]
      .map((v) =>
        y + v[1] >= N || x + v[0] >= N ? "" : board[y + v[1]][x + v[0]] == "0"
      )
      .every((v) => v)
  );

// board[y][x]
let result = 0;
const check = () => {
  if (x == +N - 1 && y == +N - 1) {
    result += 1;
  }

  const canMovedBooleanList = canMove(goIndex);

  for (let i = 0; i < canMovedBooleanList.length; i++) {
    const v = canMovedBooleanList[i];
    if (!v) continue;

    const [mx, my] = moveList[canMoveList[goIndex][i]];
    x += mx;
    y += my;
    const prevIndex = goIndex;
    goIndex = canMoveList[goIndex][i];

    check(result);

    x -= mx;
    y -= my;
    goIndex = prevIndex;
  }
};

check();
console.log(result);
