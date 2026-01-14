// @leet start
function residuePrefixes(s: string): number {
  // Track up to two distinct characters before returning
  let numDistinct = 0;
  let dist1: string | null = null;
  let dist2: string | null = null;

  let result = 0;

  for (let i = 0; i < s.length; i++) {
    if (s[i] !== dist1 && s[i] !== dist2) {
      switch (numDistinct) {
        case 0:
          dist1 = s[i];
          break;
        case 1:
          dist2 = s[i];
          break;
        default:
          // After we have ≥3 distinct characters result never increases
          return result;
      }

      numDistinct++;
    }

    result += Number((i + 1) % 3 === numDistinct);
  }

  return result;
}
// @leet end
