// 3085 사탕게임
// https://www.acmicpc.net/problem/3085

const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");
// const [N, ...input] = require("fs")
//   .readFileSync("./text.txt")
//   .toString()
//   .trim()
//   .split("\n");

const board = input.map((v) => v.split(""));
const isOverBoard = (x, y) => x == N || y == N || x == -1 || y == -1;

const canMoveList = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

const checkBoard = () => {
  let x = 0;
  let y = 0;
  const resultArr = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      resultArr.push(checkAllCase(x + i, y + j), false);
      if (i == 0 || j == 0)
        canMoveList.forEach((v) => {
          resultArr.push(checkAllCase(x + i + v[0], y + j + v[1], true));
        });
    }
  }
  return Math.max(...resultArr);
};

const checkAllCase = (x, y, changed) =>
  Math.max(
    ...canMoveList.map((v, i) =>
      check(x, y, changed, (x, y) => [x + v[0], y + v[1]], i)
    )
  );

const changedList = (arr = [], x, y, key, start, end) =>
  arr
    .map((v, i) => {
      if (!isOverBoard(x + v[0], y + v[1]))
        if (board[x + v[0]][y + v[1]] == key) {
          if (x + v[0] == N - 1 && y + v[1] == N - 1) return v;
          if (start <= i && i < end) return v;
        }
    })
    .filter((v) => v);

const check = (x, y, changed, next, index) => {
  if (isOverBoard(x, y)) return 0;

  let key = board[x][y];
  let count = 0;
  while (!isOverBoard(x, y)) {
    if (key != board[x][y]) {
      if (changed) return count;

      let start, end;
      if (index >= 2) {
        start = 0;
        end = 2;
      } else {
        start = 2;
        end = 4;
      }

      let afterValue = Math.max(
        ...changedList(canMoveList, x, y, key, start, end).map((v) => {
          const temp = board[x][y];
          board[x][y] = board[x + v[0]][y + v[1]];
          board[x + v[0]][y + v[1]] = temp;

          const countValue = check(x, y, true, next, index);

          board[x + v[0]][y + v[1]] = board[x][y];
          board[x][y] = temp;

          return countValue;
        })
      );
      if (afterValue == -Infinity) afterValue = 0;

      return afterValue + count;
    }
    count++;
    [x, y] = next(x, y);
  }
  if (!changed) return 0;
  return count;
};

console.log(checkBoard());
