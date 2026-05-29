// @leet start
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const counts = new Map();

  for (const ch of s) {
    counts.set(ch, (counts.get(ch) ?? 0) + 1);
  }

  for (const ch of t) {
    counts.set(ch, (counts.get(ch) ?? 0) - 1);
  }

  for (const count of counts.values()) {
    if (count) {
      return false;
    }
  }

  return true;
};
// @leet end
