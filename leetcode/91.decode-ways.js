// @leet start
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
  let prev = 1;
  let prevPrev = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    let curr = 0;

    if (s[i] !== "0") {
      curr = prev;

      if (
        i < s.length - 1 &&
        (s[i] === "1" || (s[i] === "2" && s[i + 1] < "7"))
      ) {
        curr += prevPrev;
      }
    }

    [prev, prevPrev] = [curr, prev];
  }

  return prev;
};
// @leet end
