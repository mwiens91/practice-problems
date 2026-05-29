// @leet start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let res = 0;
  const freqs = new Map();

  let start = 0;

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    if (freqs.get(ch)) {
      while (s[start] !== ch) {
        freqs.set(s[start], freqs.get(s[start]) - 1);
        start++;
      }

      start++;
    }

    freqs.set(ch, 1);
    res = Math.max(res, i - start + 1);
  }

  return res;
};
// @leet end
