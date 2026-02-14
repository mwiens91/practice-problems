// @leet start
function mapWordWeights(words: string[], weights: number[]): string {
  const aCharCode = "a".charCodeAt(0);
  const zCharCode = aCharCode + 25;

  return words
    .map((word) =>
      [...word].reduce(
        (accum, ch) => accum + weights[ch.charCodeAt(0) - aCharCode],
        0,
      ),
    )
    .map((weight) => String.fromCharCode(zCharCode - (weight % 26)))
    .join("");
}
// @leet end
