// @leet start
/**
 * @param {number[][]} graph
 * @return {number[]}
 */
var eventualSafeNodes = function (graph) {
  const edgesIn = Array.from({ length: graph.length }, () => []);
  const outDegree = Array(graph.length).fill(0);

  for (let i = 0; i < graph.length; i++) {
    for (const j of graph[i]) {
      edgesIn[j].push(i);
      outDegree[i]++;
    }
  }

  const stack = [];

  for (let i = 0; i < graph.length; i++) {
    if (!outDegree[i]) {
      stack.push(i);
    }
  }

  while (stack.length) {
    const node = stack.pop();

    for (const adj of edgesIn[node]) {
      outDegree[adj]--;

      if (!outDegree[adj]) {
        stack.push(adj);
      }
    }
  }

  return Array.from({ length: graph.length }, (_, i) => i).filter(
    (i) => !outDegree[i],
  );
};
// @leet end
