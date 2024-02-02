const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week8/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const distanceArray = input[1].split(" ").map((v) => BigInt(v));
const costArray = input[2].split(" ").map((v) => BigInt(v));

let answer = distanceArray[0] * costArray[0];
let cost_now = costArray[0];

for (let i = 1; i < n - 1; i++) {
  if (cost_now > costArray[i]) {
    cost_now = costArray[i];
  }
  answer += distanceArray[i] * cost_now;
}

console.log(answer.toString());

/**
 * 첫 시도에 58점이 나온 이유
 * 숫자가 너무 커서 오버플로우 발생
 * → BigInt 데이터 타입 사용하면 해결 가능
 */
