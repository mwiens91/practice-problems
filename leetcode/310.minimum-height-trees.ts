// @leet start
function findMinHeightTrees(n: number, edges: number[][]): number[] {
  if (n === 1) {
    return [0];
  }

  // Transform into undirected graph
  const graph: number[][] = Array.from({ length: n }, () => []);

  for (const edge of edges) {
    graph[edge[0]].push(edge[1]);
    graph[edge[1]].push(edge[0]);
  }

  // Get all 1-degree nodes and do something similar to Kahn's
  // algorithm
  let curr: number[] = [];
  const degree: number[] = new Array(n);

  for (const [node, edges] of graph.entries()) {
    degree[node] = edges.length;

    if (degree[node] === 1) {
      curr.push(node);
    }
  }

  while (true) {
    const next: number[] = [];

    for (const node of curr) {
      degree[node]--;

      for (const adj of graph[node]) {
        degree[adj]--;

        if (degree[adj] === 1) {
          next.push(adj);
        }
      }
    }

    if (!next.length) {
      return curr;
    }

    curr = next;
  }
}
// @leet end
