// @leet start
function minDays(bloomDay: number[], m: number, k: number): number {
  if (bloomDay.length < m * k) {
    return -1;
  }

  const isValid = (target: number) => {
    let consecutive = 0;
    let bouquetCount = 0;

    for (const day of bloomDay) {
      if (day <= target) {
        consecutive++;
      } else {
        bouquetCount += Math.floor(consecutive / k);
        consecutive = 0;
      }
    }

    bouquetCount += Math.floor(consecutive / k);

    return bouquetCount >= m;
  };

  let left = 1;
  let right = Math.max(...bloomDay);

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (isValid(mid)) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return left;
}
// @leet end
