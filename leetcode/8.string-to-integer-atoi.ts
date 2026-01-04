// @leet start
function myAtoi(s: string): number {
  let start = 0;

  while (start < s.length && s[start] === " ") {
    start++;
  }

  let sign = 1;

  if (start < s.length && "+-".includes(s[start])) {
    if (s[start] === "-") {
      sign = -1;
    }

    start++;
  }

  let end = start;

  while (end < s.length && /\d/.test(s[end])) {
    end++;
  }

  return Math.min(
    Math.max(sign * Number(s.slice(start, end)), -(2 ** 31)),
    2 ** 31 - 1,
  );
}
// @leet end
