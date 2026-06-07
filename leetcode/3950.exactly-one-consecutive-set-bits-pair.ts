// @leet start
function consecutiveSetBits(n: number): boolean {
  let numPairs = 0;
  let prev = -1;

  for (; n; n >>= 1) {
    const curr = n & 1;

    if (curr === 1 && prev === 1) {
      numPairs++;
    }

    prev = curr;
  }

  return numPairs === 1;
}
// @leet end
