// @leet start
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  const counts = new Map();

  for (ch of s) {
    counts.set(ch, 1 + (counts.get(ch) ?? 0));
  }

  for (let i = 0; i < s.length; i++) {
    if (counts.get(s[i]) === 1) {
      return i;
    }
  }

  return -1;
};
// @leet end
