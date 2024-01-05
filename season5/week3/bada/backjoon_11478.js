/**
 * 문제: 서로 다른 부분 문자열의 개수 / 11478번
 *
 * 부분 문자열 예시)
 * ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc
 *
 * 문자열이 주어졌을 때 서로 다른 부분 문자열의 개수를 구하는 문제
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week3/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const substring = new Set();

for (let i = 1; i < input.length + 1; i++) {
  for (let j = 0; j < input.length; j++) {
    if (i + j > input.length) break;
    substring.add(input.slice(j, i + j));
  }
}
console.log(substring.size);

/**
 * 많이 느리지만,, Set으로 최대한 시간복잡도를 줄어봤다.
 */
