// @leet start
function reverseWords(s: string): string {
  const tokensRev: string[] = [];

  // end is inclusive
  let end = s.length - 1;

  while (end >= 0) {
    // Skip trailing space
    while (end >= 0 && s[end] === " ") {
      end--;
    }

    if (end < 0) {
      break;
    }

    // Find start of token
    let start = end;

    while (start > 0 && s[start - 1] !== " ") {
      start--;
    }

    tokensRev.push(s.slice(start, end + 1));
    end = start - 1;
  }

  return tokensRev.join(" ");
}
// @leet end
