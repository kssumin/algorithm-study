/**
 * 문제: 종이의 개수
 *
 * N*N 크기의 행렬로 표현되는 종이
 * 종이의 각 칸에는 -1, 0, 1 중 하나가 저장
 *
 * 0 0 0 1 1 1 -1 -1 -1
 * 0 0 0 1 1 1 -1 -1 -1
 * 0 0 0 1 1 1 -1 -1 -1
 * 1 1 1 0 0 0 0 0 0
 * 1 1 1 0 0 0 0 0 0
 * 1 1 1 0 0 0 0 0 0
 * 0 1 -1 0 1 -1 0 1 -1
 * 0 -1 1 0 1 -1 0 1 -1
 * 0 1 -1 1 0 -1 0 1 -1
 *
 * -1 : 1 + 9
 * 0 : 3 + 8
 * 1 : 2 + 9
 *
 * 분할 정복 재귀,,
 * 분할 정복 ???????????????
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week9/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

let [n, ...numbers] = input;

numbers = numbers.map((v) => v.split(" "));

const result = {
  "-1": 0,
  0: 0,
  1: 0,
};

function dfs(x, y, size) {
  const check = numbers[x][y];

  for (let i = x; i < x + size; i++) {
    for (let j = y; j < y + size; j++) {
      if (numbers[i][j] !== check) {
        for (let k = 0; k < 3; k++) {
          for (let l = 0; l < 3; l++) {
            dfs(x + k * (size / 3), y + l * (size / 3), size / 3);
          }
        }
        return;
      }
    }
  }

  result[check]++;
}

dfs(0, 0, n);
console.log(`${result["-1"]}\n${result[0]}\n${result[1]}`);
