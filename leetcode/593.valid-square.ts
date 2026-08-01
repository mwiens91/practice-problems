// @leet start
function validSquare(
  p1: number[],
  p2: number[],
  p3: number[],
  p4: number[],
): boolean {
  const dists = new Set<number>();
  const points = [p1, p2, p3, p4];

  for (let i = 0; i < points.length; i++) {
    for (let j = i + 1; j < points.length; j++) {
      const x = points[i][0] - points[j][0];
      const y = points[i][1] - points[j][1];

      dists.add(x * x + y * y);
    }
  }

  return dists.size === 2 && !dists.has(0);
}
// @leet end
