// @leet start
/**
 * @param {number} n
 * @return {number}
 */
var numTilings = function (n) {
  const MOD = 1e9 + 7;

  // For the next column we iterate over, how many things are filled?
  // None or one? Hold is meant for putting down a two-stack of
  // horizontal pieces, we add it like a carry digit to "none" for the
  // next iteration.
  let none = 1;
  let one = 0;
  let hold = 0;

  for (let _ = 0; _ < n; _++) {
    [none, one, hold] = [
      (none + hold) % MOD,
      (none + one) % MOD,
      (none + 2 * one) % MOD,
    ];
  }

  return none;
};
// @leet end
