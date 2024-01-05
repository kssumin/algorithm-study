const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week4/bada/input.txt";
const inputs = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")[1]
  .split(" ");

const stack = [];
const answer = [];
for (i = inputs.length - 1; i >= 0; i--) {
  const cnt = +inputs[i];
  while (stack.length > 0 && stack[stack.length - 1] <= cnt) {
    stack.pop();
  }
  if (stack.length === 0) answer.push(-1);
  if (stack.length > 0) answer.push(stack[stack.length - 1]);
  stack.push(cnt);
}

console.log(answer.reverse().join(" "));
