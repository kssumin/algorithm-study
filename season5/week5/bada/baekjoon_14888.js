/**
 * 문제: 연산자 끼워넣기
 *
 * 일단 순열로 도전!
 *
 * 푸는데 성공했지만,,, 메모리와 시간이 너무 많이 들었다.
 * 상위권 사람들의 풀이를 참고해야 할 것 같다.
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week5/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = +input[0];
const numbers = input[1].split(" ");
const count = input[2].split(" ");

const operator = (
  "+".repeat(count[0]) +
  "-".repeat(count[1]) +
  "*".repeat(count[2]) +
  "/".repeat(count[3])
).split("");

// 순열 구현
const permutation = (current, rests, output, size) => {
  if (current.length === size) {
    output.push([...current]);
  }
  rests.forEach((v, idx) => {
    current.push(v);
    const rest = [...rests.slice(0, idx), ...rests.slice(idx + 1)];
    permutation(current, rest, output, size);
    current.pop();
  });
};

const output = [];
permutation([], operator, output, n - 1);
const unique = new Set(output.map((v) => v.join("")));

const results = [];
unique.forEach((v) => {
  for (i = 0; i < n; i++) {
    let result = +numbers[0];

    for (j = 0; j < v.length; j++) {
      switch (v[j]) {
        case "+":
          result += +numbers[j + 1];
          break;
        case "-":
          result -= +numbers[j + 1];
          break;
        case "*":
          result *= +numbers[j + 1];
          break;
        case "/":
          result = ~~(result / +numbers[j + 1]);
          break;
      }
    }
    results.push(result);
  }
});

console.log(Math.max(...results));
console.log(Math.min(...results));
