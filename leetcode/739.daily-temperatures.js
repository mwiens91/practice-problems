// @leet start
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  const result = Array(temperatures.length).fill(0);
  const monoStack = [];

  for (let i = temperatures.length - 1; i >= 0; i--) {
    const currTemp = temperatures[i];

    while (monoStack.length && monoStack[monoStack.length - 1][0] <= currTemp) {
      monoStack.pop();
    }

    if (monoStack.length) {
      result[i] = monoStack[monoStack.length - 1][1] - i;
    }

    monoStack.push([currTemp, i]);
  }

  return result;
};
// @leet end
