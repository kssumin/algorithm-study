/**
 * 문제: 가희와 키워드 / 22233번
 *
 * 가희가 메모장에 적은 키워드, 블로그 작성 시 키워드를 사용하면 그 키워드는 메모장에서 지워진다.
 * 블로그에는 메모장에 없는 키워드도 사용할 수 있다.
 *
 * 블로그 작성 후 메모장에 남은 키워드의 수를 구하라
 */

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week3/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [n, m] = input[0].split(" ").map((v) => +v);
const memo = input.slice(1, 1 + n);
const blog = input.slice(1 + n, 1 + n + m).map((v) => v.split(","));

const memoSet = new Set(memo);
const result = [];

for (const keywords of blog) {
  keywords.forEach((k) => memoSet.has(k) && memoSet.delete(k));
  result.push(memoSet.size);
}

console.log(result.join("\n"));

/**
 * Set을 사용해도 시간초과가 나서 의아했는데, for문 안에서 console.log를 해서 시간초과가 난 것이었다!
 *
 * console.log는 느리기 때문에 루프 내부에서 호출하는 것은 비효율적일 수 있다.
 * 때문에 외부에서 한 번만 호출하는게 시간초과를 해결하는 답이 되었다.
 */
