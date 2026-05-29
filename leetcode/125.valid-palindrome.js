// @leet start
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const isAlpha = (ch) => /^[a-zA-Z0-9]$/.test(ch);

  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (!isAlpha(s[left])) {
      left++;
    } else if (!isAlpha(s[right])) {
      right--;
    } else {
      if (s[left].toLowerCase() !== s[right].toLowerCase()) {
        return false;
      }

      left++;
      right--;
    }
  }

  return true;
};
// @leet end
