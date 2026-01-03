// @leet start
function evalRPN(tokens: string[]): number {
  const stack: number[] = [];

  for (const token of tokens) {
    if ("+-*/".includes(token)) {
      const b = stack.pop()!;
      const a = stack.pop()!;

      switch (token) {
        case "+":
          stack.push(a + b);
          break;
        case "-":
          stack.push(a - b);
          break;
        case "*":
          stack.push(a * b);
          break;
        default:
          stack.push(Math.trunc(a / b));
      }
    } else {
      stack.push(Number(token));
    }
  }

  return stack[0];
}
// @leet end
