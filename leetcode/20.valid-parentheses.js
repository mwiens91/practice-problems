// @leet start
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const complements = { ")": "(", "]": "[", "}": "{" };
  const stack = [];

  for (const ch of s) {
    if (Object.keys(complements).includes(ch)) {
      if (!stack.length) {
        return false;
      }

      const top = stack.pop();

      if (top !== complements[ch]) {
        return false;
      }
    } else {
      stack.push(ch);
    }
  }

  return !stack.length;
};
// @leet end
