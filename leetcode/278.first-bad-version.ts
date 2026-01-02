// @leet start
/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

const solution = function (isBadVersion: (version: number) => boolean) {
  return function (n: number): number {
    let lo = 0;
    let hi = n;

    while (lo <= hi) {
      const mid = Math.floor((lo + hi) / 2);

      if (isBadVersion(mid)) {
        hi = mid - 1;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  };
};
// @leet end
