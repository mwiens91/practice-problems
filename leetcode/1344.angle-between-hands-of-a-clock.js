// @leet start
/**
 * @param {number} hour
 * @param {number} minutes
 * @return {number}
 */
var angleClock = function (hour, minutes) {
  const diff = 6 * Math.abs(5 * hour - (11 / 12) * minutes);

  return diff > 180 ? 360 - diff : diff;
};
// @leet end
