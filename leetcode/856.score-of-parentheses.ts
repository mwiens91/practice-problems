// @leet start
function scoreOfParentheses(s: string): number {
  const stack: number[] = [];

  for (const ch of s) {
    if (ch === "(") {
      stack.push(0);
    } else if (stack[stack.length - 1] === 0) {
      stack[stack.length - 1]++;
    } else {
      let sum = 0;

      while (stack[stack.length - 1] !== 0) {
        sum += stack.pop()!;
      }

      stack[stack.length - 1] = 2 * sum;
    }
  }

  return stack.reduce((acc, curr) => acc + curr);
}
// @leet end
