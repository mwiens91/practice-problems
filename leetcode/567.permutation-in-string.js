// @leet start
/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function (s1, s2) {
  const CODE_POINT_A = "a".codePointAt(0);
  const charToIdx = (ch) => ch.codePointAt(0) - CODE_POINT_A;
  const s1Counts = Array(26).fill(0);

  for (ch of s1) {
    s1Counts[charToIdx(ch)]++;
  }

  const windowCounts = Array(26).fill(0);

  for (let i = 0; i < s2.length; i++) {
    windowCounts[charToIdx(s2[i])]++;

    if (i >= s1.length - 1) {
      let okay = true;

      for (let j = 0; j < 26; j++) {
        if (s1Counts[j] !== windowCounts[j]) {
          okay = false;
          break;
        }
      }

      if (okay) {
        return true;
      }

      windowCounts[charToIdx(s2[i - s1.length + 1])]--;
    }
  }

  return false;
};
// @leet end
