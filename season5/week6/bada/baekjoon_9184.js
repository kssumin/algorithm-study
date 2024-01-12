/**
 * 문제 : 신나는 함수 실행
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week6/bada/input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" "));

const SIZE = 21;

let x = new Array(SIZE);
for (let i = 0; i < SIZE; i++) {
  x[i] = new Array(SIZE);
  for (var j = 0; j < SIZE; j++) {
    x[i][j] = new Array(SIZE).fill(null);
  }
}

const calculator = (a, b, c) => {
  if (a <= 0 || b <= 0 || c <= 0) {
    return 1;
  }
  if (a > 20 || b > 20 || c > 20) {
    return calculator(20, 20, 20);
  }
  if (x[a][b][c]) {
    return x[a][b][c];
  }

  if (a < b && b < c) {
    x[a][b][c] =
      calculator(a, b, c - 1) +
      calculator(a, b - 1, c - 1) -
      calculator(a, b - 1, c);
    return x[a][b][c];
  }

  x[a][b][c] =
    calculator(a - 1, b, c) +
    calculator(a - 1, b - 1, c) +
    calculator(a - 1, b, c - 1) -
    calculator(a - 1, b - 1, c - 1);
  return x[a][b][c];
};

const answer = input
  .slice(0, input.length - 1)
  .map(
    (v) => `w(${v[0]}, ${v[1]}, ${v[2]}) = ${calculator(+v[0], +v[1], +v[2])}`
  )
  .join("\n");
console.log(answer);
