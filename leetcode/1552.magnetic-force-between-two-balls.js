// @leet start
/**
 * @param {number[]} position
 * @param {number} m
 * @return {number}
 */
var maxDistance = function (position, m) {
  position.sort((a, b) => a - b);

  const isValid = (target) => {
    let remaining = m - 1;
    let prev = position[0];
    let i = 1;

    while (remaining && i < position.length) {
      if (position[i] - prev >= target) {
        remaining--;
        prev = position[i];
      }

      i++;
    }

    return remaining === 0;
  };

  let low = 1;
  let high = Math.floor(
    (position[position.length - 1] - position[0]) / (m - 1),
  );

  while (low <= high) {
    const mid = low + Math.floor((high - low) / 2);

    if (isValid(mid)) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }

  return high;
};
// @leet end
