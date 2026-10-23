// @leet start
/**
 * @param {string[]} words
 * @return {number}
 */
var longestPalindrome = function (words) {
  const counts = Array.from({ length: 26 }, () => Array(26).fill(0));
  const getChIdx = (ch) => ch.codePointAt(0) - "a".codePointAt(0);

  for (const word of words) {
    const i = getChIdx(word[0]);
    const j = getChIdx(word[1]);
    counts[i][j]++;
  }

  let pairs = 0;
  let extra = 0;

  for (let i = 0; i < 26; i++) {
    pairs += Math.floor(counts[i][i] / 2);
    extra |= counts[i][i] % 2;

    for (let j = i + 1; j < 26; j++) {
      pairs += Math.min(counts[i][j], counts[j][i]);
    }
  }

  return 2 * (2 * pairs + extra);
};
// @leet end
