/**
 * 문제: 파도반 수열
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week6/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const t = +input[0];
const nList = input.slice(1).map((v) => +v);

const dp = new Array(101);

dp[0] = 1;
dp[1] = 1;
dp[2] = 1;
dp[3] = 2;
dp[4] = 2;

for (let i = 5; i < 101; i++) {
  dp[i] = dp[i - 1] + dp[i - 5];
}

const answer = [];
nList.forEach((v) => answer.push(dp[v - 1]));
console.log(answer.join("\n"));
