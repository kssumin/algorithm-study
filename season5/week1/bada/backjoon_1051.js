/**
 * 문제: 숫자 정사각형
 * 넓혀나가며 구하지말고 좁혀가며 구하기,,!
 *
 */
const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "backjoon_1051/input.txt";
const [nm, ...input] = fs.readFileSync(filePath).toString().trim().split("\n");
const [n, m] = nm.split(" ").map((v) => +v);
const arr = input.map((v) => v.split("").map((v) => +v));
const size = n > m ? n : m;

let isFind = false;

outer: for (let k = size; k > 0; k--) {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (
        i + k < n &&
        j + k < m &&
        arr[i][j] === arr[i][j + k] &&
        arr[i][j] === arr[i + k][j] &&
        arr[i][j] === arr[i + k][j + k]
      ) {
        console.log((k + 1) * (k + 1));
        isFind = true;
        break outer;
      }
    }
  }
}

!isFind && console.log(1);
