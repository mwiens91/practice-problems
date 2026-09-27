// @leet start
/**
 * // Definition for a _Node.
 * function _Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {_Node} node
 * @return {_Node}
 */
var cloneGraph = function (node) {
  if (!node) {
    return null;
  }

  const cloneMap = new Map();
  const toProcess = [node];
  const processed = new Set();

  cloneMap.set(node, new _Node(node.val));

  while (toProcess.length) {
    const orig = toProcess.pop();
    const clone = cloneMap.get(orig);

    for (const origNeighbor of orig.neighbors) {
      if (!cloneMap.has(origNeighbor)) {
        cloneMap.set(origNeighbor, new _Node(origNeighbor.val));
        toProcess.push(origNeighbor);
      }

      clone.neighbors.push(cloneMap.get(origNeighbor));
    }

    processed.add(orig);
  }

  return cloneMap.get(node);
};
// @leet end
