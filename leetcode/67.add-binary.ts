// @leet start
function addBinary(a: string, b: string): string {
  const resultReversed: string[] = [];
  let carry = 0;

  for (let i = a.length - 1, j = b.length - 1; i >= 0 || j >= 0; i--, j--) {
    const val =
      carry +
      (i >= 0 && a[i] === "1" ? 1 : 0) +
      (j >= 0 && b[j] === "1" ? 1 : 0);
    resultReversed.push(String(val % 2));
    carry = Math.floor(val / 2);
  }

  if (carry) {
    resultReversed.push("1");
  }

  return resultReversed.reverse().join("");
}
// @leet end
