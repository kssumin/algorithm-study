/**
 * 문제: 5568번 카드놓기
 *
 * n과 k의 크기가 크지 않다.
 * 4 <= n <= 10 / 2 <= k <= 4
 *
 * 시간복잡도가 팩토리얼도 가능함.
 * → nPk(순열)로 모든 경우를 구하고 그 값을 Set에 추가하자
 * → 최종적으로 Set의 size가 정답
 *
 * 문제는! JS로 순열 구현하기~~~
 */

// 입력
const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week5/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, k, ...numbers] = input;

// 생성한 정수를 저장하는 Set
const result = new Set();

// 순열 구현
const permutation = (current, rests, output, size) => {
  if (rests.length === size) {
    return output.push(current);
  }
  rests.forEach((v, idx) => {
    const rest = [...rests.slice(0, idx), ...rests.slice(idx + 1)];
    permutation([...current, v], rest, output, size);
  });
};

// 문제 풀이
const size = Number(n - k);

const output = [];
permutation([], numbers, output, size);
output.forEach((v) => result.add(v.join("")));

console.log(result.size);
