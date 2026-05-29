// @leet start
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let i = 0;

  while (true) {
    if (i >= strs[0].length) {
      break;
    }

    const target = strs[0][i];
    let done = false;

    for (let j = 1; j < strs.length; j++) {
      if (i >= strs[j].length || strs[j][i] !== target) {
        done = true;
        break;
      }
    }

    if (done) {
      break;
    }

    i++;
  }

  return strs[0].slice(0, i);
};

// @leet end
