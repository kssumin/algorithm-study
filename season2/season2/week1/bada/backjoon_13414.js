/**
 * 13414번 - 수강신청
 * 난이도 - 실버 3
 * 알고리즘 분류 -
 */

// 입력
/*
const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s/);
const k = parseInt(input[0]);
const l = parseInt(input[1]);
const arr = input.slice(2);*/

/*const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s/);*/

const input = require("fs")
  .readFileSync("./week1/bada/example/input.txt")
  .toString()
  .trim()
  .split("\n");
const nums = input.map((v) => v.split(" "));
const k = nums[0].shift();
const l = nums[0].shift();
nums.shift();

let arr = []; //입력값이 저장되는 배열
for (let i = 0; i < l; i++) {
  arr.push(nums[i][0]);
}
// Map 자료형을 이용한 해시 선언
let hash = new Map();
arr.map((it) => {
  if (hash.has(it)) {
    hash.delete(it);
  }
  hash.set(it, 1);
});

let count = 0;
let answer = [];

hash.forEach((value, key) => {
  if (count < k) {
    answer.push(key);
    count++;
  }
});

console.log(answer.join("\n"));
