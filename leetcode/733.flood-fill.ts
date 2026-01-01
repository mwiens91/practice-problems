// @leet start
function floodFill(
  image: number[][],
  sr: number,
  sc: number,
  color: number,
): number[][] {
  const origColor = image[sr][sc];

  if (origColor === color) {
    return image;
  }

  const stack: [number, number][] = [[sr, sc]];

  while (stack.length) {
    const [r, c] = stack.pop()!;

    if (
      r >= 0 &&
      r < image.length &&
      c >= 0 &&
      c < image[0].length &&
      image[r][c] === origColor
    ) {
      image[r][c] = color;

      stack.push([r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]);
    }
  }

  return image;
}
// @leet end
