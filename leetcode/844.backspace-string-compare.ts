// @leet start
function backspaceCompare(s: string, t: string): boolean {
  const processString = (s: string): string => {
    const stack: string[] = [];

    for (const c of s) {
      if (c === "#") {
        stack.pop();
      } else {
        stack.push(c);
      }
    }

    return stack.join("");
  };

  return processString(s) === processString(t);
}
// @leet end
