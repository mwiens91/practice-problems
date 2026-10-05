// @leet start
function minRotations(s: string): number {
  let curr = 0;
  let count = 0;

  for (const ch of s) {
    const dig = Number(ch);
    count += Math.min((10 + dig - curr) % 10, (10 + curr - dig) % 10);
    curr = dig;
  }

  return count;
}
// @leet end
