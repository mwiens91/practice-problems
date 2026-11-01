// @leet start
function shortestPalindrome(s: string): string {
  // LPS for s
  const lps: number[] = Array(s.length).fill(0);
  let l = 0;

  for (let i = 1; i < s.length; i++) {
    while (l > 0 && s[i] !== s[l]) {
      l = lps[l - 1];
    }

    if (s[i] === s[l]) {
      l++;
      lps[i] = l;
    }
  }

  // Continue on 3rd part of s + # + reversed(s)
  // NOTE: no need to fill up the array for this part
  l = 0;

  for (let i = s.length - 1; i >= 0; i--) {
    while (l > 0 && s[i] !== s[l]) {
      l = lps[l - 1];
    }

    if (s[i] === s[l]) {
      l++;
    }
  }

  return [...[...s.slice(l)].reverse(), s].join("");
}
// @leet end
