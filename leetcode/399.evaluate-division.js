// @leet start
/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function (equations, values, queries) {
  const adjLists = new Map(); // Map<string, [string, number][]>

  for (let i = 0; i < equations.length; i++) {
    const [a, b] = equations[i];
    const val = values[i];

    if (!adjLists.has(a)) {
      adjLists.set(a, []);
    }

    if (!adjLists.has(b)) {
      adjLists.set(b, []);
    }

    adjLists.get(a).push([b, val]);
    adjLists.get(b).push([a, 1 / val]);
  }

  const answerQuery = (c, d) => {
    if (!adjLists.has(c) || !adjLists.has(d)) {
      return -1;
    }

    const stack = [[c, 1]];
    const seen = new Set([c]);

    while (stack.length) {
      const [curr, weight] = stack.pop();

      if (curr === d) {
        return weight;
      }

      for (const [adj, edgeWeight] of adjLists.get(curr) ?? []) {
        if (!seen.has(adj)) {
          seen.add(adj);
          stack.push([adj, weight * edgeWeight]);
        }
      }
    }

    return -1;
  };

  const result = [];

  for (const [c, d] of queries) {
    result.push(answerQuery(c, d));
  }

  return result;
};
// @leet end
