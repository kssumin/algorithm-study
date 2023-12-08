/**
 * 문제: 배 / 1092번
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week3/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const limits = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
const m = +input[2];
const boxes = input[3]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

if (limits.slice(-1)[0] < boxes.slice(-1)[0]) {
  console.log(-1);
  return;
}

let answer = 0;

while (boxes.length > 0) {
  for (let i = n - 1; i >= 0; i--) {
    for (let j = boxes.length - 1; j >= 0; j--) {
      if (limits[i] >= boxes[j]) {
        boxes.splice(j, 1);
        break;
      }
    }
  }
  answer++;
}

console.log(answer);

/**
 * 93%에서 시간초과
 *
 * 계속 시간초과가 나서 다른 사람 코드를 봤다...
 * 뭐가 문제였는지 비교해봐야 될 것 같다.
 */
