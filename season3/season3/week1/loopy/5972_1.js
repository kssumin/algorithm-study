// 5972 택배 배송
// https://www.acmicpc.net/problem/5972

// const [NM, ...input] = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .trim()
//   .split("\n");
const [NM, ...input] = require("fs")
  .readFileSync("./text.txt")
  .toString()
  .trim()
  .split("\n");

const [N, M] = NM.split(" ").map((v) => +v);
const maps = input
  .map((s) => s.split(" ").map((v) => +v))
  .map((v) => (v[0] > v[1] ? [v[1], v[0], v[2]] : v))
  .sort();

const dp = Array.from({ length: N + 1 }, () =>
  Array.from({ length: N + 1 }, () => Infinity)
);

maps.forEach((v) => {
  const [from, to, value] = v;
  dp[from][to] = value;
  dp[to][from] = value;
});

const solve = () => {
  for (let i = 1; i < N + 1; i++) {
    for (let j = 1; j < N + 1; j++) {
      if (dp[i][j] != Infinity) {
        for (let k = 1; k < N + 1; k++) {
          const minValues = Math.min(dp[k][j], dp[i][j] + dp[i][k]);
          dp[k][j] = minValues;
          dp[j][k] = minValues;
        }
      }
    }
  }
};

solve();
// console.log(dp.splice(1).join("\n"));
console.log(dp[N][1]);
