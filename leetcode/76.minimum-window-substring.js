// @leet start
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  const OFFSET = "A".codePointAt(0);

  // (counts in t) - (counts in window)
  const countsDiff = Array("z".codePointAt(0) - OFFSET + 1).fill(0);

  let numInvalid = 0;

  for (const ch of t) {
    const idx = ch.codePointAt(0) - OFFSET;

    if (countsDiff[idx] === 0) {
      numInvalid++;
    }

    countsDiff[idx]++;
  }

  let bestLength = Infinity;
  let bestLeft = -1;
  let bestRight = -1;

  for (let left = 0, right = 0; right < s.length; right++) {
    // add right
    const rightChIdx = s[right].codePointAt(0) - OFFSET;
    countsDiff[rightChIdx]--;

    if (countsDiff[rightChIdx] === 0) {
      numInvalid--;
    }

    if (!numInvalid) {
      // move up left
      while (countsDiff[s[left].codePointAt(0) - OFFSET] < 0) {
        countsDiff[s[left].codePointAt(0) - OFFSET]++;
        left++;
      }

      // update solution
      const currLength = right - left + 1;

      if (currLength < bestLength) {
        bestLength = currLength;
        bestLeft = left;
        bestRight = right;
      }
    }
  }

  return bestLength < Infinity ? s.slice(bestLeft, bestRight + 1) : "";
};
// @leet end
