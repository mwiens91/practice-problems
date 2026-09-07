// @leet start
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  const lastSeen = new Map(); // index at which we've last seen char
  let start = 0;
  let best = 0;

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];

    // Move up start if needed
    if (lastSeen.has(ch)) {
      const lastIdx = lastSeen.get(ch);

      if (lastIdx >= start) {
        start = lastIdx + 1;
      }
    }

    // Mark down this character's index
    lastSeen.set(ch, i);

    // Update result
    best = Math.max(best, i - start + 1);
  }

  return best;
};
// @leet end
