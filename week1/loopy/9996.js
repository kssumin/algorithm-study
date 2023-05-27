// 9996 한국이 그리울 땐 서버에 접속하지 // solved
// https://www.acmicpc.net/problem/9996

const [N, keyword, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
// const [N, keyword, ...input] = require("fs")
//   .readFileSync("./text.txt")
//   .trim()
//   .split("\n");

const [head, tail] = keyword.split("*");

input.forEach((v) => {
  if (
    v.indexOf(head) == 0 &&
    v.lastIndexOf(tail) + tail.length == v.length &&
    v.length >= keyword.length - 1
  ) {
    console.log("DA");
  } else {
    console.log("NE");
  }
});
