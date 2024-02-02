// 문자열 S가 주어졌을 때 세준이의 뒤집기 방법으로 만들 수 있는 문자열 중 사전순으로 제일 앞서는 것 출력

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week4/bada/input.txt";
const s = fs.readFileSync(filePath).toString().trim().split("");

let s1 = s[0];

for (i = 1; i < s.length; i++) {
  if (s1[i - 1] < s[i]) {
    s1 = s[i] + s1;
    continue;
  }
  s1 = s1 + s[i];
}

console.log(s1.split("").reverse().join(""));
