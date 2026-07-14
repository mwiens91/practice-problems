// @leet start
function secondsBetweenTimes(startTime: string, endTime: string): number {
  const helper = (t: string) =>
    3600 * Number(t.slice(0, 2)) +
    60 * Number(t.slice(3, 5)) +
    Number(t.slice(6));

  return helper(endTime) - helper(startTime);
}
// @leet end
