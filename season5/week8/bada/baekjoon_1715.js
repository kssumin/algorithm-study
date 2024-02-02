// 우선순위 큐 (최소 힙)
class PriorityQueue {
  constructor() {
    this.heap = [];
  }

  // swap(a, b) → a와 b의 위치를 바꾼다.
  swap(a, b) {
    const temp = this.heap[a];
    this.heap[a] = this.heap[b];
    this.heap[b] = temp;
  }

  // queue에 value를 추가한다.
  push(value) {
    const { heap } = this;
    heap.push(value);
    let index = heap.length - 1;
    let parent = Math.floor((index - 1) / 2);

    while (index > 0 && heap[index] < heap[parent]) {
      this.swap(index, parent);
      index = parent;
      parent = Math.floor((index - 1) / 2);
    }
  }

  //
  pop() {
    const { heap } = this;
    if (heap.length <= 1) {
      return heap.pop();
    }

    const output = heap[0];
    heap[0] = heap.pop();
    let index = 0;

    while (index * 2 + 1 < heap.length) {
      let left = index * 2 + 1;
      let right = index * 2 + 2;
      let next = index;

      if (heap[left] < heap[next]) {
        next = left;
      }

      if (right < heap.length && heap[right] < heap[next]) {
        next = right;
      }

      if (index === next) {
        break;
      }

      this.swap(index, next);
      index = next;
    }

    return output;
  }
}

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week8/bada/input.txt";
const [N, ...cards] = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const queue = new PriorityQueue();
let count = 0;

cards.forEach((card) => {
  queue.push(card);
});

while (queue.heap.length > 1) {
  const sum = queue.pop() + queue.pop();
  queue.push(sum);
  count += sum;
}

console.log(count);
