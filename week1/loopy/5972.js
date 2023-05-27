// 5972 택배 배송
// https://www.acmicpc.net/problem/5972
// 다익스트라 알고리즘 queue 버전(https://80000coding.oopy.io/2bf224f0-3e62-433d-b11f-7ef32144e50b)

// const [NM, ...input] = require("fs")
//   .readFileSync("/dev/stdin")
//   .toString()
//   .split("\n");
const [NM, ...input] = require("fs")
  .readFileSync("./text.txt")
  .toString()
  .trim()
  .split("\n");

const graph = [];

input
  .map((s) => s.split(" ").map(Number))
  .forEach((v) => {
    const [from, to, dist] = v;
    if (graph[from] == undefined) graph[from] = [];
    if (graph[to] == undefined) graph[to] = [];
    graph[from].push({ to, dist });
    graph[to].push({ to: from, dist });
  });

const queue = [{ to: 1, dist: 0 }];
const dist = Array(graph.length).fill(Infinity);
dist[1] = 0;

while (queue.length) {
  const p = queue.pop();
  const { to } = p;

  if (dist[to] < p.dist) continue;

  graph[to].forEach((next) => {
    const acc = dist[to] + next.dist;
    if (dist[next.to] > acc) {
      dist[next.to] = acc;
      queue.push(next);
    }
  });
}

console.log(dist[dist.length - 1]);
