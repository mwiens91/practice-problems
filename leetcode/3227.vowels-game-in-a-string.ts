// @leet start
function doesAliceWin(s: string): boolean {
  const VOWELS = new Set(["a", "e", "i", "o", "u"]);

  return [...s].some((ch) => VOWELS.has(ch));
}
// @leet end
