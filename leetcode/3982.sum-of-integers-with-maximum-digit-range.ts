// @leet start
function maxDigitRange(nums: number[]): number {
  let maxRange = 0;
  let maxRangeSum = 0;

  for (const num of nums) {
    const range = getDigitRange(num);

    if (range > maxRange) {
      maxRange = range;
      maxRangeSum = num;
    } else if (range === maxRange) {
      maxRangeSum += num;
    }
  }

  return maxRangeSum;
}

function getDigitRange(num: number): number {
  let maxDigit = 0;
  let minDigit = 9;

  for (; num > 0; num = Math.floor(num / 10)) {
    const digit = num % 10;

    maxDigit = Math.max(maxDigit, digit);
    minDigit = Math.min(minDigit, digit);
  }

  return Math.max(maxDigit - minDigit, 0);
}
// @leet end
