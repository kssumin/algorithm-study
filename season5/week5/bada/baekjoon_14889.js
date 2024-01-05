/**
 * 문제: 스타터와 링크
 *
 * 아직 백트래킹에 대해 감을 못 잡겠다...!
 */

// 입력
const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week5/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, ...table] = input.map((v) => v.split(" ").map((i) => Number(i)));
const people = Array.from({ length: n }, (v, i) => i);

const START = [];
let LINK = [];
const visited = Array.from({ length: n }, () => 0);
let min = Number.MAX_SAFE_INTEGER;

function dfs(count, start) {
  if (count === n / 2) {
    LINK = remainPeople(people, START);
    const startPoint = calcTeamPoint(table, START);
    const linkPoint = calcTeamPoint(table, LINK);
    min = Math.min(min, Math.abs(startPoint - linkPoint));
    return;
  }

  for (let i = start; i < n; i++) {
    if (visited[i]) continue;
    visited[i] = true;
    START.push(i);
    dfs(count + 1, i);
    START.pop();
    visited[i] = false;
  }
}

/**
 * people 중 team 포함되지 않은 요소들을 구하는 함수
 * @param {number[]} people
 * @param {number[]} team
 * @returns
 */
function remainPeople(people, team) {
  return people.filter((v) => !team.includes(v));
}

/**
 * 각 팀의 능력치를 구한다.
 * @param {number[][]} points 점수표
 * @param {number[]} team 팀원
 * @returns
 */
function calcTeamPoint(points, team) {
  let result = 0;
  for (let i = 0; i < team.length; i++) {
    for (let j = 0; j < team.length; j++) {
      if (i === j) continue;
      result += points[team[i]][team[j]];
    }
  }
  return result;
}

dfs(0, 0);
console.log(min);
