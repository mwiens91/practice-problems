// @leet start
function totalFruit(fruits: number[]): number {
  const lastSeenIdx: number[] = [];
  let left = 0;
  let best = 0;

  for (let i = 0; i < fruits.length; i++) {
    if (fruits[i] === fruits[lastSeenIdx[0]]) {
      lastSeenIdx[0] = i;
    } else if (fruits[i] === fruits[lastSeenIdx[1]]) {
      lastSeenIdx[1] = i;
    } else if (lastSeenIdx.length < 2) {
      lastSeenIdx.push(i);
    } else {
      best = Math.max(best, i - left);

      let toRemoveBasketIdx = Number(lastSeenIdx[0] > lastSeenIdx[1]);
      left = lastSeenIdx[toRemoveBasketIdx] + 1;

      lastSeenIdx[toRemoveBasketIdx] = i;
    }
  }

  best = Math.max(best, fruits.length - left);

  return best;
}
// @leet end
