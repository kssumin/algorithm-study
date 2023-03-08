/**
 * 10816번 - 숫자 카드 2
 * 난이도 - 실버 4
 * 알고리즘 분류 - 자료 구조, 정렬, 이분 탐색, 해스를 사용한 집합과 맵
 */

// 입력
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s/)
  .map(Number);
const n = parseInt(input[0]);
const n_arr = input.slice(1, n + 1);
const [m, ...m_arr] = input.slice(n + 1);

// n_arr 순회하면서 hash table(객체) 완성
const hash = {};

n_arr.map((it) => {
  hash.hasOwnProperty(it) ? (hash[it] += 1) : (hash[it] = 1);
});

// m_arr 순회하면서 hash에 key 존재하면 value 출력, 존재하지 않으면 0 출력
const answer = [];
m_arr.map((it) => {
  hash.hasOwnProperty(it) ? answer.push(hash[it]) : answer.push(0);
});

console.log(answer.join(" "));
