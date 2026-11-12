// @leet start
/**
 * @param {string} s
 * @param {number[][]} pairs
 * @return {string}
 */
var smallestStringWithSwaps = function (s, pairs) {
  const parent = Array.from({ length: s.length }, (_, i) => i);
  const size = Array(s.length).fill(1);

  const find = (a) => {
    if (parent[a] === a) {
      return a;
    }

    parent[a] = find(parent[a]);
    return parent[a];
  };
  const union = (a, b) => {
    const rootA = find(a);
    const rootB = find(b);

    if (rootA === rootB) {
      return;
    }

    const [small, big] =
      size[rootA] <= size[rootB] ? [rootA, rootB] : [rootB, rootA];

    parent[small] = big;
    size[big] += size[small];
  };

  for (const [a, b] of pairs) {
    union(a, b);
  }

  const components = Array.from({ length: s.length }, () => []);

  for (let i = 0; i < s.length; i++) {
    components[find(i)].push(i);
  }

  // Rearrange characters in each component
  const sArr = [...s];

  for (const component of components) {
    const sorted = component.map((i) => sArr[i]).sort();

    // NOTE: indices are in ascending order by construction
    component.forEach((i, j) => (sArr[i] = sorted[j]));
  }

  return sArr.join("");
};
// @leet end
