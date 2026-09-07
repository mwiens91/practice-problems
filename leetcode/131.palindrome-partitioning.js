// @leet start
/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function (s) {
  const res = []; //string[][]
  let curr = [];

  const isPalindrome = (start, end) => {
    let left = start;
    let right = end - 1;

    while (left < right) {
      if (s[left] !== s[right]) {
        return false;
      }

      left++;
      right--;
    }

    return true;
  };

  const backtrack = (start, i) => {
    if (i === s.length) {
      if (start === s.length) {
        res.push([...curr]);
      }

      return;
    }

    if (isPalindrome(start, i + 1)) {
      curr.push(s.slice(start, i + 1));
      backtrack(i + 1, i + 1);
      curr.pop();
    }

    // and try not taking it
    backtrack(start, i + 1);
  };

  backtrack(0, 0);

  return res;
};
// @leet end
