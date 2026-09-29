// @leet start
/**
 * @param {number[]} cookies
 * @param {number} k
 * @return {number}
 */
var distributeCookies = function (cookies, k) {
  cookies.sort((a, b) => b - a);

  // Set best to some feasible result to allow more early pruning
  let best = 0;

  for (let i = 0; i < cookies.length - k + 1; i++) {
    best += cookies[i];
  }

  const dist = Array(k).fill(0);

  const backtrack = (i) => {
    if (i === cookies.length) {
      best = Math.min(best, Math.max(...dist));
      return;
    }

    const seen = new Set();

    for (let j = 0; j < dist.length; j++) {
      if (dist[j] + cookies[i] >= best || seen.has(dist[j])) {
        continue;
      }

      seen.add(dist[j]);

      dist[j] += cookies[i];
      backtrack(i + 1);
      dist[j] -= cookies[i];
    }
  };

  backtrack(0);

  return best;
};
// @leet end
