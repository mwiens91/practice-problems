// @leet start
/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
var numMatchingSubseq = function (s, words) {
  const getCharIdx = (ch) => ch.codePointAt(0) - "a".codePointAt(0);
  const charIdxs = Array.from({ length: 26 }, () => []);

  for (let i = 0; i < s.length; i++) {
    charIdxs[getCharIdx(s[i])].push(i);
  }

  let result = 0;

  for (const word of words) {
    let sIdx = 0;
    let okay = true;

    for (const ch of word) {
      const idxs = charIdxs[getCharIdx(ch)];

      let left = 0;
      let right = idxs.length - 1;

      while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);

        if (idxs[mid] < sIdx) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      }

      if (left === idxs.length) {
        okay = false;
        break;
      }

      sIdx = idxs[left] + 1;
    }

    if (okay) {
      result++;
    }
  }

  return result;
};
// @leet end
