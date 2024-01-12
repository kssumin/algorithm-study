/**
 * 문제: 게단 오르기
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week6/bada/input.txt";
const input = fs.readFileSync(filePath).toString().split("\n");

const n = +input[0];
const floor = input.slice(1).map((v) => +v);

const SIZE = 301;
const dp = new Array(SIZE);

dp[0] = floor[0];
dp[1] = floor[0] + floor[1];
dp[2] = Math.max(floor[0] + floor[2], floor[1] + floor[2]);

for (let i = 3; i < n + 1; i++) {
  dp[i] = Math.max(dp[i - 3] + floor[i - 1] + floor[i], dp[i - 2] + floor[i]);
}

console.log(dp[n - 1]);
