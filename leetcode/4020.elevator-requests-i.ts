// @leet start
function elevatorRequests(n: number, requests: number[]): number {
  let res = requests[0];

  for (let i = 1; i < requests.length; i++) {
    res += Math.abs(requests[i] - requests[i - 1]);
  }

  return res;
}
// @leet end
