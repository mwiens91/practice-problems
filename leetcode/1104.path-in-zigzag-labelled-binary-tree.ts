// @leet start
function pathInZigZagTree(label: number): number[] {
  const pathToRoot = [label];
  let curr = label;
  let parentRowSize = (1 << Math.floor(Math.log2(label))) >> 1; // :)

  while (parentRowSize > 0) {
    curr = 3 * parentRowSize - 1 - (curr >> 1);
    pathToRoot.push(curr);
    parentRowSize >>= 1;
  }

  return pathToRoot.reverse();
}
// @leet end
