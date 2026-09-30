// @leet start
/**
 * @param {number[]} dist
 * @param {number} hour
 * @return {number}
 */
var minSpeedOnTime = function (dist, hour) {
  if (dist.length - 1 >= hour) {
    return -1;
  }

  const isValid = (v) => {
    let time = 0;

    for (let i = 0; i < dist.length - 1; i++) {
      time += Math.ceil(dist[i] / v);
    }

    time += dist[dist.length - 1] / v;

    return time <= hour;
  };

  const maxDist = Math.max(...dist);
  let left = 1;
  let right =
    hour >= dist.length ? maxDist : maxDist / (hour - Math.floor(hour));

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (isValid(mid)) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
};
// @leet end
