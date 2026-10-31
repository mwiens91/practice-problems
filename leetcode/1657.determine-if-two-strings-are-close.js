// @leet start
/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function (word1, word2) {
  if (word1.length !== word2.length) {
    return false;
  }

  const getChIdx = (ch) => ch.codePointAt(0) - "a".codePointAt(0);
  const getCounts = (s) => {
    const counts = Array(26).fill(0);

    for (const ch of s) {
      counts[getChIdx(ch)]++;
    }

    return counts;
  };

  // Assert distinct characters are the same
  const word1Counts = getCounts(word1);
  const word2Counts = getCounts(word2);

  for (let i = 0; i < 26; i++) {
    if (Boolean(word1Counts[i]) !== Boolean(word2Counts[i])) {
      return false;
    }
  }

  // Assert count of counts of characters are the same
  const countOfCountsMap = new Map();

  const modifyCoCMap = (counts, add = true) => {
    for (const count of counts) {
      countOfCountsMap.set(
        count,
        (add ? 1 : -1) + (countOfCountsMap.get(count) ?? 0),
      );
    }
  };

  modifyCoCMap(word1Counts, true);
  modifyCoCMap(word2Counts, false);

  for (const countOfCount of countOfCountsMap.values()) {
    if (countOfCount) {
      return false;
    }
  }

  return true;
};
// @leet end
