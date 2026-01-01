// @leet start
function isPalindrome(s: string): boolean {
  const alphanum = /[a-zA-Z\d]/;
  let i = 0;
  let j = s.length - 1;

  while (i < j) {
    if (!alphanum.test(s[i])) {
      i++;
      continue;
    }

    if (!alphanum.test(s[j])) {
      j--;
      continue;
    }

    if (s[i].toLowerCase() !== s[j].toLowerCase()) {
      return false;
    }

    i++;
    j--;
  }

  return true;
}
// @leet end
