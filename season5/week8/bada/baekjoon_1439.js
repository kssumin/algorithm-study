const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week8/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("");

let summary = input[0];
for (let i = 1; i < input.length; i++) {
  if (input[i] !== input[i - 1]) {
    summary += input[i];
  }
}

console.log(parseInt(summary.length / 2));
