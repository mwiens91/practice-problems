// @leet start
function rearrangeString(s: string, x: string, y: string): string {
  const res = [...s];
  let left = 0; // invariant: left points to first non-y char

  while (left < res.length && res[left] === y) {
    left++;
  }

  for (let i = left; i < res.length; i++) {
    if (res[i] === y) {
      [res[left], res[i]] = [res[i], res[left]];
      left++;
    }
  }

  return res.join("");
}
// @leet end
