// @leet start
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  const CODE_POINT_A = "A".codePointAt(0);
  const counts = Array(26).fill(0);

  const isValid = () => {
    let maxCount = 0;
    let totalCount = 0;

    for (i = 0; i < 26; i++) {
      if (counts[i] > maxCount) {
        maxCount = counts[i];
      }

      totalCount += counts[i];
    }

    return totalCount - maxCount <= k;
  };

  let left = 0;
  let best = 0;

  for (let right = 0; right < s.length; right++) {
    // Add in right character
    counts[s[right].codePointAt(0) - CODE_POINT_A]++;

    // Shrink the window until valid
    while (!isValid()) {
      counts[s[left].codePointAt(0) - CODE_POINT_A]--;
      left++;
    }

    // Update best
    best = Math.max(best, right - left + 1);
  }

  return best;
};
// @leet end
