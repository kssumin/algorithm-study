/**
 * 문제: 주사위 쌓기
 *
 * 조건
 * - 위에 있는 주사위의 아랫면에 적힌 숫자 === 아래에 있는 주사위의 윗면에 적힌 숫자
 * - 주사위를 위,아래 고정한 채 옆으로 90 / 180 / 270도 돌릴 수 있음
 * - A, B, C, D, E, F 순서로 입력
 *
 * 어...어렵다!
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week2/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim();

const dices = input
  .split("\n")
  .slice(1)
  .map((i) => i.split(" "));

const other = {
  0: 5,
  1: 3,
  2: 4,
  3: 1,
  4: 2,
  5: 0,
};

const answer = [];

for (let i = 0; i < 6; i++) {
  let diceNum = [1, 2, 3, 4, 5, 6];
  const upperSide = dices[0][i];
  let bottomSide = dices[0][other[i]];
  diceNum = diceNum.filter((n) => n !== +upperSide && n !== +bottomSide);

  answer.push(Math.max(...diceNum));

  for (let j = 1; j < dices.length; j++) {
    let nextNum = [1, 2, 3, 4, 5, 6];
    const nextUpperSide = bottomSide;
    const nextBottomSideIndex = other[dices[j].indexOf(bottomSide)];
    const nextBottomSide = dices[j][nextBottomSideIndex];
    bottomSide = nextBottomSide;
    nextNum = nextNum.filter(
      (n) => n !== +nextUpperSide && n !== +nextBottomSide
    );

    answer[i] = answer[i] + Math.max(...nextNum);
  }
}

console.log(Math.max(...answer));
