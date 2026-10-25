// @leet start
function calculateScore(a: number, b: number): number {
  const getSetBits = (n: number) => {
    let res = 0;

    while (n) {
      n &= n - 1;
      res++;
    }

    return res;
  };

  const s1 = getSetBits(a);
  const s2 = getSetBits(b);

  return s1 >= s2 ? s1 * s2 : Math.floor(s2 / s1);
}
// @leet end
