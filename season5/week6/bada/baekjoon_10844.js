/**
 * 문제: 쉬운 계단 수
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week6/bada/input.txt";
const n = fs.readFileSync(filePath).toString().trim();

const SIZE = 101;
const MOD = 1000000000;

let dp = new Array(SIZE);
for (let i = 0; i < SIZE; i++) {
  dp[i] = new Array(10).fill(null);
}

// 초기 세팅
dp[1][0] = 0;
for (let i = 1; i < 10; i++) {
  dp[1][i] = 1;
}

for (let i = 2; i <= n; i++) {
  for (let j = 0; j < 10; j++) {
    if (j === 0) {
      if (dp[i][j] === null) dp[i][j] = dp[i - 1][1] % MOD;
    }
    if (j === 9) {
      if (dp[i][j] === null) dp[i][j] = dp[i - 1][8] % MOD;
    }
    if (j > 0 && j < 9) {
      if (dp[i][j] === null)
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD;
    }
  }
}

let answer = dp[n].reduce((a, b) => (a + b) % MOD, 0);
console.log(answer);
