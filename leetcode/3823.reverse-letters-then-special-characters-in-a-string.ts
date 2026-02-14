// @leet start
function reverseByType(s: string): string {
  const chars = [...s];

  const reverseByPred = (pred: (ch: string) => boolean) => {
    let left = 0;
    let right = chars.length - 1;

    while (left < right) {
      while (left < right && !pred(chars[left])) {
        left++;
      }

      while (left < right && !pred(chars[right])) {
        right--;
      }

      [chars[left], chars[right]] = [chars[right], chars[left]];
      left++;
      right--;
    }
  };

  reverseByPred((ch) => ch >= "a" && ch <= "z");
  reverseByPred((ch) => ch < "a" || ch > "z");

  return chars.join("");
}
// @leet end
