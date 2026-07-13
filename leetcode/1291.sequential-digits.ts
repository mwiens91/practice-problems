// @leet start
function sequentialDigits(low: number, high: number): number[] {
  const minDigits = Math.floor(Math.log10(low)) + 1;
  const maxDigits = Math.floor(Math.log10(high)) + 1;
  const res: number[] = [];

  for (let k = minDigits; k <= maxDigits; k++) {
    for (let i = 1; i < 10 - k + 1; i++) {
      let num = 0;

      for (let j = 0; j < k; j++) {
        num += (i + j) * 10 ** (k - j - 1);
      }

      if (num < low) {
        continue;
      } else if (num > high) {
        break;
      }

      res.push(num);
    }
  }

  return res;
}
// @leet end
