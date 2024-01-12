const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "backjoon_1543/input.txt";
const [docs, keyword] = fs.readFileSync(filePath).toString().trim().split("\n");

let start = 0;
let count = 0;

while (start < docs.length) {
  const result = docs.slice(start).indexOf(keyword);
  if (result === -1) {
    break;
  } else {
    start = start + result + keyword.length;
    count++;
  }
}

console.log(count);
