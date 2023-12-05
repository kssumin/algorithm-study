/**
 * 문제: 좌표 압축
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week2/bada/input.txt";
const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")[1]
  .split(" ");

Array.prototype.removeDuplication = function () {
  return [...new Set(this)];
};

const dict = new Map();

[...input]
  .sort((a, b) => a - b)
  .removeDuplication()
  .map((i, index) => dict.set(i, index));

const answer = input.map((i) => dict.get(i));
console.log(answer.join(" "));

/**
 * 시간 초과
 * → filter로 검색하는 과정에서 시간이 많이 소요되는 것 같다.
 * → Map 자료형을 사용해보자
 *
 * Map 사용하니까 시간 초과 안 난다!
 *
 * 내가 만든 함수도 매서드 체이닝 해보고 싶어서 시도한 prototype 조작
 * 알고리즘을 자바스크립트로 푸니까 이런 저런 도전을 할 수 있어서 좋은 것 같다.
 */
