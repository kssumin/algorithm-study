/**
 * 문제: 추월 / 2002번
 *
 * 터널에 들어가는 차량 순서와 터널에서 나오는 차량 순서를 보고 터널 내에서 추월을 한 차량을 찾아내는 문제
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week3/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const inputCar = input.slice(1, 1 + n);
const outputCar = input.slice(1 + n).map((v) => inputCar.indexOf(v));

const stack = [];

for (const order of outputCar) {
  while (stack[stack.length - 1] > order && stack.length > 0) {
    stack.pop();
  }
  stack.push(order);
}

console.log(inputCar.length - stack.length);

/**
 * 스택으로 풀어보자!!!!
 */
