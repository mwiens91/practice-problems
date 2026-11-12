// @leet start
/**
 * @param {number[][]} edges
 * @param {number} bob
 * @param {number[]} amount
 * @return {number}
 */
var mostProfitablePath = function (edges, bob, amount) {
  const n = amount.length;
  const adjLists = Array.from({ length: n }, () => []);

  for (const [a, b] of edges) {
    adjLists[a].push(b);
    adjLists[b].push(a);
  }

  const path = [];
  const bobDfs = (node, parent) => {
    path.push(node);

    if (node === 0) {
      return true;
    }

    for (const adj of adjLists[node]) {
      if (adj !== parent && bobDfs(adj, node)) {
        return true;
      }
    }

    path.pop();
    return false;
  };
  bobDfs(bob, -1);

  // Adjust costs based on Bob's path
  const medianIdx = Math.floor(path.length / 2);

  for (let i = 0; i < medianIdx; i++) {
    amount[path[i]] = 0;
  }

  if (path.length % 2 === 1) {
    amount[path[medianIdx]] /= 2;
  }

  const aliceDfs = (node, parent) => {
    let best = -Infinity;

    for (const adj of adjLists[node]) {
      if (adj !== parent) {
        best = Math.max(best, aliceDfs(adj, node));
      }
    }

    return (best > -Infinity ? best : 0) + amount[node];
  };

  return aliceDfs(0, -1);
};
// @leet end
