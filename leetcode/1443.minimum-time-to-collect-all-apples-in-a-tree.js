// @leet start
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {boolean[]} hasApple
 * @return {number}
 */
var minTime = function (n, edges, hasApple) {
  const adjLists = Array.from({ length: n }, () => []);

  for (const [a, b] of edges) {
    adjLists[a].push(b);
    adjLists[b].push(a);
  }

  const dfs = (node, parent = -1) => {
    let result = 0;

    for (const child of adjLists[node]) {
      if (child !== parent) {
        childVal = dfs(child, node);

        if (hasApple[child] || childVal > 0) {
          result += 2 + childVal;
        }
      }
    }

    return result;
  };

  return dfs(0);
};
// @leet end
