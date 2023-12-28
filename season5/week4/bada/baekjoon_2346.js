const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week4/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let n = +input[0];
const balloons = input[1].split(" ").map((v, index) => [index + 1, +v]);

const calcIndex = (a, b, max) => {
  if (a + b < 0) {
    return a + b + max;
  }
  if (a + b > max - 1) {
    return a + b - max;
  }
  return a + b;
};

let cnt = 0;
let target;

const answer = [];

while (balloons.length > 0) {
  const [idx, value] = balloons[cnt];
  target = calcIndex(cnt, value, n);
  n--;
  balloons.splice(cnt, 1);
  answer.push(idx);
  if (target > cnt) target--;
  cnt = target;
}

console.log(answer.join(" "));

/* 메모리 초과 */
