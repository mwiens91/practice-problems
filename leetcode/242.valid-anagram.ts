// @leet start
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) {
    return false;
  }

  // Counts will contain for each char freq(s) - freq(t)
  const counts: Map<string, number> = new Map();

  for (const c of s) {
    counts.set(c, (counts.get(c) ?? 0) + 1);
  }

  for (const c of t) {
    if (!counts.has(c)) {
      return false;
    }

    const newVal = counts.get(c)! - 1;

    if (newVal < 0) {
      return false;
    }

    if (newVal === 0) {
      counts.delete(c);
    } else {
      counts.set(c, newVal);
    }
  }

  return counts.size === 0;
}
// @leet end
