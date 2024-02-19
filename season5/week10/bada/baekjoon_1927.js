/**
 * 문제: 최소 힙
 */

class MinHeap {
  constructor() {
    this.heap = [];
  }

  size() {
    return this.heap.length;
  }

  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  // 삽입 연산
  add(value) {
    this.heap.push(value);
    this.bubbleUp();
  }

  // 삭제 연산
  poll() {
    if (this.heap.length === 0) {
      return 0;
    }
    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const value = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown();
    return value;
  }

  /**
   * 새로 들어온 노드가 최소 힙의 조건에 맞는 자리를 찾도록 도와주는 메서드
   */
  bubbleUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      // 새로 들어온 값의 자리부터 시작하여 index 값이 0이 될 때까지 부모 노드와 비교 반복
      const parentIndex = Math.floor((index - 1) / 2);
      if (this.heap[parentIndex] <= this.heap[index]) break;
      this.swap(index, parentIndex);
      index = parentIndex;
    }
  }

  /**
   * 루트 노드를 제거한 후 최소 힙의 조건에 맞도록 힙을 재정비하는 메소드
   */
  bubbleDown() {
    let index = 0;
    const length = this.heap.length;

    while (true) {
      let smallest = index;
      const leftChildIndex = 2 * index + 1;
      const rightChildIndex = 2 * index + 2;

      if (
        leftChildIndex < length &&
        this.heap[leftChildIndex] < this.heap[smallest]
      ) {
        smallest = leftChildIndex;
      }

      if (
        rightChildIndex < length &&
        this.heap[rightChildIndex] < this.heap[smallest]
      ) {
        smallest = rightChildIndex;
      }

      if (smallest === index) break;
      this.swap(index, smallest);
      index = smallest;
    }
  }
}

const fs = require("fs");
const filePath =
  process.platform === "linux" ? "/dev/stdin" : "season5/week10/bada/input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [_, ...nums] = input.map((v) => +v);
const minHeap = new MinHeap();
const answer = [];

for (const num of nums) {
  if (num === 0) {
    answer.push(minHeap.poll());
  } else {
    minHeap.add(num);
  }
}

console.log(answer.join("\n"));
