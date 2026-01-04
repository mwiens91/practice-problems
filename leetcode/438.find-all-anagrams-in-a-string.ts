// @leet start
function findAnagrams(s: string, p: string): number[] {
  if (p.length > s.length) {
    return [];
  }

  // Set up a map which holds the difference between counts in p and
  // counts in the window
  const countsDelta = new Map<string, number>();

  for (const c of p) {
    countsDelta.set(c, (countsDelta.get(c) ?? 0) + 1);
  }

  let end = 0;

  for (; end < p.length; end++) {
    if (countsDelta.has(s[end])) {
      countsDelta.set(s[end], countsDelta.get(s[end])! - 1);
    }
  }

  // Slide the window
  const result: number[] = [];
  const processWindow = () => {
    for (const count of countsDelta.values()) {
      if (count !== 0) {
        return;
      }
    }

    result.push(end - p.length);
  };

  for (; end < s.length; end++) {
    processWindow();

    const first = end - p.length;

    if (countsDelta.has(s[first])) {
      countsDelta.set(s[first], countsDelta.get(s[first])! + 1);
    }

    if (countsDelta.has(s[end])) {
      countsDelta.set(s[end], countsDelta.get(s[end])! - 1);
    }
  }

  processWindow();

  return result;
}
// @leet end
