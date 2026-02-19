// @leet start
function toggleLightBulbs(bulbs: number[]): number[] {
  const bulbOn = Array.from({ length: 100 }, () => false);

  for (const bulb of bulbs) {
    bulbOn[bulb - 1] = !bulbOn[bulb - 1];
  }

  return bulbOn.reduce((accum, isOn, idx) => {
    if (isOn) {
      accum.push(idx + 1);
    }
    return accum;
  }, [] as number[]);
}
// @leet end
