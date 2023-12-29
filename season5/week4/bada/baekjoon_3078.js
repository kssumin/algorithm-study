const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week4/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");
const [N, K] = input[0].split(" ");
const students = input.slice(1).map((v) => v.length);

const map = new Map();

for (i = 2; i < 21; i++) {
  map.set(i, 0);
}

let end = 0;
let answer = 0;
while (end < N) {
  if (end > K) {
    const popLength = students[end - K - 1];
    map.set(popLength, map.get(popLength) - 1);
  }
  const addLength = students[end];
  answer += map.get(addLength);
  map.set(addLength, map.get(addLength) + 1);
  end++;
}

console.log(answer);
