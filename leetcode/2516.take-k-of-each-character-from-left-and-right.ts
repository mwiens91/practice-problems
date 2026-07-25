// @leet start
function takeCharacters(s: string, k: number): number {
  const CODE_POINT_A = "a".codePointAt(0)!;
  const getIdx = (ch: string) => ch.charCodeAt(0) - CODE_POINT_A;
  const counts = Array(3).fill(0);

  for (const ch of s) {
    counts[getIdx(ch)]++;
  }

  if (counts.some((count) => count < k)) {
    return -1;
  }

  let left = 0;
  let res = s.length;

  for (let right = 0; right < s.length; right++) {
    counts[getIdx(s[right])]--;

    while (counts.some((count) => count < k)) {
      counts[getIdx(s[left])]++;
      left++;
    }

    res = Math.min(res, s.length - right - 1 + left);
  }

  return res;
}
// @leet end
