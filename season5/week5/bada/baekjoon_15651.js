/**
 * 문제: N과 M(3)
 *
 * 이 문제는 중복 순열을 구현하는 문제!!
 * 5568번 (카드놓기) 에서 구현한 순열 코드를 이용해보자
 *
 * 시간 초과가 나서 슬펐지만, console.log를 한 번에 하자 시간 초과가 해결되었다!!!!
 * 알고리즘 풀 때는 최대한 console.log를 호출하는 횟수를 줄이기
 */

// 입력
const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week5/bada/input.txt";
const [n, m] = fs.readFileSync(filePath).toString().trim().split(" ");

const numbers = Array.from({ length: +n }, (v, i) => i + 1);

// 중복 순열 구현
const permuteRepeat = (current, rests, output, size) => {
  if (current.length === size) {
    return output.push(current);
  }
  rests.forEach((v) => {
    permuteRepeat([...current, v], rests, output, size);
  });
};

const output = [];
permuteRepeat([], numbers, output, +m);

const answer = [];
output.forEach((v) => answer.push(v.join(" ")));
console.log(answer.join("\n"));
