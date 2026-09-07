// @leet start
/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
  const getTime = (pos, speed) => (target - pos) / speed;

  const positionSpeed = position.map((x, i) => [x, speed[i]]);
  positionSpeed.sort((a, b) => b[0] - a[0]);

  let result = 1;
  let prevTime = getTime(...positionSpeed[0]);

  for (let i = 1; i < positionSpeed.length; i++) {
    const currTime = getTime(...positionSpeed[i]);

    if (currTime > prevTime) {
      result++;
      prevTime = currTime;
    }
  }

  return result;
};
// @leet end
