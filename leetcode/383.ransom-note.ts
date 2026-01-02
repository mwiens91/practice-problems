// @leet start
function canConstruct(ransomNote: string, magazine: string): boolean {
  if (ransomNote.length > magazine.length) {
    return false;
  }

  const counts: Map<string, number> = new Map();

  for (const c of magazine) {
    counts.set(c, (counts.get(c) ?? 0) + 1);
  }

  for (const c of ransomNote) {
    if (!counts.has(c)) {
      return false;
    }

    const newCount = counts.get(c)! - 1;
    counts.set(c, newCount);

    if (!newCount) {
      counts.delete(c);
    }
  }

  return true;
}
// @leet end
