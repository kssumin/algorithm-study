/**
 * 문제: 듣보잡 / 1764번
 * 듣도 못한 사람 리스트와 보도 못한 사람 리스트를 보고 듣도 보도 못한 사람을 찾는 문제
 */
const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week3/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map((v) => +v);

const unheard = input.slice(1, 1 + n);
const unseen = input.slice(1 + n, 1 + n + m);

const unheardMap = new Map();
unheard.forEach((v) => unheardMap.set(v, v));

const result = unseen.filter((v) => unheardMap.get(v)).sort();

console.log(result.length);
console.log(result.join("\n"));

/**
 * 배열에서 그냥 값을 찾았을 땐 시간초과가 났다.
 * Map을 사용했더니 시간초과는 해결됐다.
 */
