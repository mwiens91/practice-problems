// @leet start
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var checkIfPrerequisite = function (numCourses, prerequisites, queries) {
  const adjLists = Array.from({ length: numCourses }, () => []);

  for (const [parent, child] of prerequisites) {
    adjLists[parent].push(child);
  }

  const reachableSets = Array(numCourses).fill(null);

  const getReachableSet = (node) => {
    if (reachableSets[node] !== null) {
      return reachableSets[node];
    }

    let reachableSet = new Set();

    for (const child of adjLists[node]) {
      reachableSet.add(child);
      reachableSet = reachableSet.union(getReachableSet(child));
    }

    reachableSets[node] = reachableSet;

    return reachableSets[node];
  };

  return queries.map(([parent, child]) => getReachableSet(parent).has(child));
};
// @leet end
