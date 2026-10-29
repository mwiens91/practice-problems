// @leet start
function reachableNodes(
  n: number,
  edges: number[][],
  restricted: number[],
): number {
  const adjLists: number[][] = Array.from({ length: n }, () => []);

  for (const [a, b] of edges) {
    adjLists[a].push(b);
    adjLists[b].push(a);
  }

  const stack: number[] = [0];
  const available: boolean[] = Array(n).fill(true);
  available[0] = false;
  restricted.forEach((i) => (available[i] = false));

  let result = 0;

  while (stack.length) {
    const node = stack.pop()!;
    result++;

    for (const adj of adjLists[node]) {
      if (available[adj]) {
        stack.push(adj);
        available[adj] = false;
      }
    }
  }

  return result;
}
// @leet end
