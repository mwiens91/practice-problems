// @leet start
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function (numCourses, prerequisites) {
  const adjLists = Array.from({ length: numCourses }, () => []);
  const inDegree = Array(numCourses).fill(0);

  for (const [dest, src] of prerequisites) {
    adjLists[src].push(dest);
    inDegree[dest]++;
  }

  let curr = [];

  for (let i = 0; i < numCourses; i++) {
    if (!inDegree[i]) {
      curr.push(i);
    }
  }

  const result = [];

  while (curr.length) {
    const next = [];

    for (const src of curr) {
      result.push(src);

      for (const dest of adjLists[src]) {
        inDegree[dest]--;

        if (!inDegree[dest]) {
          next.push(dest);
        }
      }
    }

    curr = next;
  }

  return result.length == numCourses ? result : [];
};
// @leet end
