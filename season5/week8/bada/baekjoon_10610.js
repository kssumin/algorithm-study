const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week8/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const getAnswer = (numbers) => {
  if (!numbers.includes(0)) {
    return -1;
  }

  const sumValue = numbers.reduce((a, c) => a + c, 0);
  if (sumValue % 3 !== 0) {
    return -1;
  }

  return numbers.sort((a, b) => b - a).join("");
};

const numberArray = input.split("").map((v) => +v);

console.log(getAnswer(numberArray));

/**
 * 0이 존재하며, 3의 배수가 되는 조건 (모든 수의 합이 3의 배수)을 만족하면 존재
 * → 가장 큰 수는 정렬하기만 하면 된다!
 */
