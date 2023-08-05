// 11403 경로 찾기 // solved
// https://www.acmicpc.net/problem/11403

const [N, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .split("\n");
// const [N, ...input] = require("fs")
//   .readFileSync("./text.txt")
//   .toString()
//   .split("\n");

const graph = input.map((v) => v.split(" ").map((v) => +v));

const solution = (N, graph) => {
  const result = Array.from({ length: N }, () =>
    Array.from({ length: N }).fill(0)
  );

  for (let i = 0; i < N; i++) {
    const visited = Array(N).fill(false);
    const queue = [i];

    while (queue.length) {
      const cur = queue.shift();

      for (let j = 0; j < N; j++) {
        if (graph[cur][j] && !visited[j]) {
          visited[j] = true;
          queue.push(j);
          result[i][j] = 1;
        }
      }
    }
  }

  return result.map((v) => v.join(" ")).join("\n");
};

console.log(solution(N, graph));
