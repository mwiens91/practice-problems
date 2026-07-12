// @leet start
function combine(n: number, k: number): number[][] {
  const res: number[][] = [];
  const curr: number[] = [];

  const backtrack = (i: number) => {
    if (curr.length === k) {
      res.push([...curr]);

      return;
    }

    for (let j = i; j <= n - (k - curr.length) + 1; j++) {
      curr.push(j);
      backtrack(j + 1);
      curr.pop();
    }
  };

  backtrack(1);

  return res;
}
// @leet end
