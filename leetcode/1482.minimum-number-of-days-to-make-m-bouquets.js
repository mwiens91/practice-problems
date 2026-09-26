// @leet start
/**
 * @param {number[]} bloomDay
 * @param {number} m
 * @param {number} k
 * @return {number}
 */
// This should already be loaded in LeetCode environment
// const { Deque } = require('@datastructures-js/deque');

var minDays = function (bloomDay, m, k) {
  if (m * k > bloomDay.length) {
    return -1;
  }

  // Get maximum value for run length starting at index i. Uses
  // monotonic deque holding indices in current window in decreasing
  // order of value.
  const runLengthMaxAtIdx = [];
  const monoDeque = new Deque();

  for (let i = 0; i < bloomDay.length; i++) {
    while (monoDeque.size() && monoDeque.front() <= i - k) {
      monoDeque.popFront();
    }

    while (monoDeque.size() && bloomDay[monoDeque.back()] <= bloomDay[i]) {
      monoDeque.popBack();
    }

    monoDeque.pushBack(i);

    if (i >= k - 1) {
      runLengthMaxAtIdx.push(bloomDay[monoDeque.front()]);
    }
  }

  // DP to find main result
  let prev = Array(bloomDay.length + 1).fill(0);

  for (let i = 1; i <= m; i++) {
    const curr = Array(bloomDay.length - i * k + 1).fill(0);

    for (j = curr.length - 1; j >= 0; j--) {
      curr[j] = Math.min(
        j < curr.length - 1 ? curr[j + 1] : Infinity,
        Math.max(runLengthMaxAtIdx[j], prev[j + k]),
      );
    }

    prev = curr;
  }

  return prev[0];
};
// @leet end
