// @leet start
/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function (tasks, n) {
  const counts = new Map();
  let maxCount = 0;
  let numWithMax = 0;

  for (const task of tasks) {
    const newCount = 1 + (counts.get(task) ?? 0);
    counts.set(task, newCount);

    if (newCount === maxCount) {
      numWithMax++;
    } else if (newCount > maxCount) {
      maxCount = newCount;
      numWithMax = 1;
    }
  }

  return Math.max((n + 1) * (maxCount - 1) + numWithMax, tasks.length);
};
// @leet end
