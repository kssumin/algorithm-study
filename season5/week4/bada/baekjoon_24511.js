const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week4/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const queueValue = [];

const aArray = input[1].split(" ");
input[2].split(" ").forEach((value, idx) => {
  if (+aArray[idx] === 0) queueValue.push(value);
});

const m = +input[3];
const inputs = input[4].split(" ");

const answer = [...queueValue.reverse(), ...inputs].splice(0, m);

console.log(answer.join(" "));
