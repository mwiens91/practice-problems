// @leet start
function vowelConsonantScore(s: string): number {
  let vowels = 0;
  let consonants = 0;

  for (const ch of s) {
    if ("aeiou".includes(ch)) {
      vowels++;
    } else if (ch >= "a" && ch <= "z") {
      consonants++;
    }
  }

  return consonants ? Math.floor(vowels / consonants) : 0;
}
// @leet end
