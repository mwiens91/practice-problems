// @leet start
/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function (weights, days) {
  const isValid = (capacity) => {
    let extraDays = days - 1;
    let currCapacity = capacity;

    for (const weight of weights) {
      if (weight > capacity) {
        return false;
      }

      if (weight > currCapacity) {
        if (extraDays === 0) {
          return false;
        }

        extraDays--;
        currCapacity = capacity;
      }

      currCapacity -= weight;
    }

    return true;
  };

  let left = Math.max(...weights);
  let right = weights.reduce((acc, w) => acc + w);

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (isValid(mid)) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
};
// @leet end
