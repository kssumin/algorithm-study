// 17070 파이프 옮기기 1 // solved
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

const dp = Array.from({ length: N }, () =>
  Array.from({ length: N }, () => [0, 0, 0])
);

dp[0][1][0] = 1;

const solve = () => {
  for (let x = 0; x < N; x++) {
    for (let y = 0; y < N; y++) {
      if (board[y][x] == 1) continue;
      if (x != 0) dp[y][x][0] += dp[y][x - 1][0] + dp[y][x - 1][1];
      if (y != 0) dp[y][x][2] += dp[y - 1][x][1] + dp[y - 1][x][2];
      if (x != 0 && y != 0)
        if (board[y - 1][x] == 0 && board[y][x - 1] == 0)
          dp[y][x][1] +=
            dp[y - 1][x - 1][0] + dp[y - 1][x - 1][1] + dp[y - 1][x - 1][2];
    }
  }
  return dp[N - 1][N - 1].reduce((a, b) => a + b, 0);
};

console.log(solve());
