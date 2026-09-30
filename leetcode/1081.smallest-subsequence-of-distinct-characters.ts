// @leet start
function smallestSubsequence(s: string): string {
  const CODE_POINT_A = "a".codePointAt(0)!;
  const getIdx = (ch: string) => ch.codePointAt(0)! - CODE_POINT_A;

  const lastIdx = Array(26).fill(0);
  const inUse = Array(26).fill(false);

  for (let i = 0; i < s.length; i++) {
    lastIdx[getIdx(s[i])] = i;
  }

  const monoStack: string[] = [];

  for (let i = 0; i < s.length; i++) {
    const chIdx = getIdx(s[i]);

    if (inUse[chIdx]) {
      continue;
    }

    // If we can do better with the current character and we can grab
    // the last entry on the stack sometime later, pop it
    while (
      monoStack.length &&
      s[i] < monoStack[monoStack.length - 1] &&
      i < lastIdx[getIdx(monoStack[monoStack.length - 1])]
    ) {
      const ch = monoStack.pop()!;
      inUse[getIdx(ch)] = false;
    }

    monoStack.push(s[i]);
    inUse[chIdx] = true;
  }

  return monoStack.join("");
}
// @leet end
