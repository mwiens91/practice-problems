// @leet start
/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var findRedundantConnection = function (edges) {
  const parent = Array.from({ length: edges.length + 1 }, (_, i) => i);
  const size = Array(edges.length + 1).fill(1);

  // Find root; do path compression
  const findRoot = (node) => {
    if (parent[node] === node) {
      return node;
    }

    parent[node] = findRoot(parent[node]);

    return parent[node];
  };

  // Union sets; union by size
  const union = (node1, node2) => {
    const root1 = findRoot(node1);
    const root2 = findRoot(node2);
    const [small, big] =
      size[root1] < size[root2] ? [root1, root2] : [root2, root1];

    size[big] += size[small];
    parent[small] = big;
  };

  const isConnected = (node1, node2) => {
    const root1 = findRoot(node1);
    const root2 = findRoot(node2);

    return root1 === root2;
  };

  for (const [node1, node2] of edges) {
    if (isConnected(node1, node2)) {
      return [node1, node2];
    }

    union(node1, node2);
  }
};
// @leet end
