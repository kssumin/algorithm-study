/**
 * 문제 : 좌표 정렬하기
 * 2차원 좌표 정렬
 * 기준
 * 1순위. x좌표 오름차순
 * 2순위. y좌표 오름차순
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week2/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n").slice(1);

const coord = input.map((i) => i.split(" "));

coord.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
console.log(coord.map((c) => c.join(" ")).join("\n"));

/**
 * js sort()에서 다중 정렬 조건 설정하는 방법
 *
 * data.sort((a, b) => 첫번째 조건 || 두번째 조건 || 세번째 조건 ...);
 */
