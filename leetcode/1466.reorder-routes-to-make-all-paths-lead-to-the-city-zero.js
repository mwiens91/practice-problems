// @leet start
/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function (n, connections) {
  // Each adjacency lists consists of edges [node, BOOL] where BOOL is
  // true if the edge is directed towards the node, else false
  const adjLists = Array.from({ length: n }, () => []);

  for (const [src, dst] of connections) {
    adjLists[src].push([dst, true]);
    adjLists[dst].push([src, false]);
  }

  const seen = Array(n).fill(false);
  seen[0] = true;
  let res = 0;

  const dfs = (node) => {
    for (const [adj, forward] of adjLists[node]) {
      if (!seen[adj]) {
        seen[adj] = true;
        res += Number(forward);
        dfs(adj);
      }
    }
  };

  dfs(0);

  return res;
};
// @leet end
