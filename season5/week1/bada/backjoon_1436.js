/**
 * 세상의 종말 영화 제목
 * 6이 적어도 3개 이상 연속으로 들어가는 수
 *
 * n 번째 영화 제목에 들어간 수 출력
 *
 * 오호라,,, 어렵다
 * 모르겠음
 *
 * n666 -> 10 / 666n -> 10 / n666m -> 100 / nm666 -> 100
 *
 * 브루트포스라고?!
 *
 * 계속 시간 초과가 났다.
 * 이유 : while 문에서 input이 string이여서 cnt !== input 조건이 만족되는 순간이 오지 않음
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "backjoon_1436/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

let cnt = 0;
let result = 666;

while (true) {
  if (String(result).includes("666")) cnt++;
  if (cnt === +input) break;
  result++;
}

console.log(result);
