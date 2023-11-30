/**
 * 문제: 소트인사이드
 * 정렬 문제
 * 수가 주어지면 그 수의 각 자리수를 내림차순으로 정렬
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week2/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const answer = input
  .split("")
  .map((i) => +i)
  .sort((a, b) => b - a)
  .join("");

console.log(answer);

/**
 * 1. split("") : string인 input을 배열로 변환
 * 2. map((i) => +i) : 각 배열 요소를 number type으로 변환
 * 3. sort((a, b) => b - a) : 내림차순으로 정렬
 * 4. join("") : 배열을 문자열로 변환
 */
