const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week2/bada/input.txt";
const s = fs.readFileSync(filePath).toString().trim();

const reverseString = (str) => str.split("").reverse().join("");
const isPalindrom = (str) => {
  return str === reverseString(str);
};

for (let i = 0; i < s.length; i++) {
  if (isPalindrom(s.slice(i))) {
    const palindrom = s + reverseString(s.slice(0, i));
    console.log(palindrom.length);
    break;
  }
}

/**
 * reverseString: 문자열을 뒤집는 함수
 * isPalindrom: 인자로 받은 문자열이 팰린드롬인지 확인하는 함수
 *
 * 1. 입력 받은 문자열 s의 각 `부분 문자열`이 팰린드롬인지 확인
 * 2. 만약 `부분 문자열`이 팰린드롬이라면, 원래 문자열의 시작부터 해당 부분 문자열의 시작까지(`s.slice(0, i)`)를 뒤집어 원래 문자열 뒤에 붙인다.
 * 3. 이렇게 하면 전체 문자열이 팰린드롬이 된다.
 * 4. 생성된 팰린드롬의 길이를 출력한다.
 */
