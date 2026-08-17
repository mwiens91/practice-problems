// @leet start
function nearestDrone(drones: number[][], target: number[]): number {
  let best = -1;
  let bestDist = Infinity;

  for (let i = 0; i < drones.length; i++) {
    const dist =
      Math.abs(target[0] - drones[i][0]) + Math.abs(target[1] - drones[i][1]);

    if (dist <= drones[i][2] && dist < bestDist) {
      best = i;
      bestDist = dist;
    }
  }

  return best;
}
// @leet end
