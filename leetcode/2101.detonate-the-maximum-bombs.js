// @leet start
/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function (bombs) {
  const adjLists = Array.from({ length: bombs.length }, () => []);

  for (let i = 0; i < bombs.length; i++) {
    const [xi, yi, ri] = bombs[i];

    for (let j = 0; j < i; j++) {
      const [xj, yj, rj] = bombs[j];
      const distSq = (xi - xj) ** 2 + (yi - yj) ** 2;

      if (ri ** 2 >= distSq) {
        adjLists[i].push(j);
      }

      if (rj ** 2 >= distSq) {
        adjLists[j].push(i);
      }
    }
  }

  const reachable = (initV) => {
    const seen = new Set([initV]);
    const stack = [initV];

    while (stack.length) {
      const v = stack.pop();

      for (const adjV of adjLists[v]) {
        if (!seen.has(adjV)) {
          seen.add(adjV);
          stack.push(adjV);
        }
      }
    }

    return seen;
  };

  // Process in order of descending outdegree
  const toProcess = Array.from({ length: bombs.length }, (_, i) => i).sort(
    (a, b) => adjLists[b].length - adjLists[a].length,
  );

  let processed = new Set();
  let best = 0;

  for (const v of toProcess) {
    if (!processed.has(v)) {
      const reached = reachable(v);
      best = Math.max(best, reached.size);
      processed = processed.union(reached);
    }
  }

  return best;
};
// @leet end
