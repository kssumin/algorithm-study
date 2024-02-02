const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week8/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const caseList = input.slice(1).map((v) => v.split(" ").map((v) => +v));

const getAnswer = (n, rankList) => {
  let answer = 1;
  let rank_now = rankList[0][1];
  for (let i = 1; i < rankList.length; i++) {
    if (rankList[i][1] < rank_now) {
      answer += 1;
      rank_now = rankList[i][1];
    }
  }
  return answer;
};

for (let i = 0; i < caseList.length; i++) {
  if (caseList[i].length === 1) {
    const n = caseList[i][0];
    const result = getAnswer(
      n,
      caseList.slice(i + 1, i + 1 + n).sort((a, b) => a[0] - b[0])
    );
    console.log(result);
  }
}
