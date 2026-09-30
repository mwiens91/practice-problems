// @leet start
function maxDepthAfterSplit(seq: string): number[] {
  const result: number[] = [];
  let depth = 0;

  for (const ch of seq) {
    if (ch === "(") {
      result.push(depth % 2);
      depth++;
    } else {
      // ch === ")"
      depth--;
      result.push(depth % 2);
    }
  }

  return result;
}
// @leet end
