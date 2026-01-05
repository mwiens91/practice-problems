// @leet start
function restoreArray(adjacentPairs: number[][]): number[] {
  const graph = new Map<number, number[]>();

  for (const edge of adjacentPairs) {
    for (const i of [0, 1]) {
      if (!graph.has(edge[i])) {
        graph.set(edge[i], []);
      }
    }

    graph.get(edge[0])!.push(edge[1]);
    graph.get(edge[1])!.push(edge[0]);
  }

  // Get a degree 1 vertex
  let prev = -1;

  for (const [v, edges] of graph.entries()) {
    if (edges.length === 1) {
      prev = v;
      break;
    }
  }

  // Traverse graph
  const n = adjacentPairs.length + 1;
  const result = [prev];
  let curr = graph.get(prev)![0];

  while (result.length < n) {
    result.push(curr);

    const edges = graph.get(curr)!;
    [prev, curr] = [curr, edges[0] === prev ? edges[1] : edges[0]];
  }

  return result;
}
// @leet end
