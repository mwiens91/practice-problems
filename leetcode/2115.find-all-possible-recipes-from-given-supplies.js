// @leet start
/**
 * @param {string[]} recipes
 * @param {string[][]} ingredients
 * @param {string[]} supplies
 * @return {string[]}
 */
var findAllRecipes = function (recipes, ingredients, supplies) {
  const adjLists = new Map();

  for (let i = 0; i < recipes.length; i++) {
    adjLists.set(recipes[i], ingredients[i]);
  }

  const suppliesSet = new Set(supplies);
  const memo = new Map();
  const visited = new Set();

  const canMake = (r) => {
    if (memo.has(r)) {
      return memo.get(r);
    }

    // If r is in visited, it's also up in the call stack, so we'll
    // set up its memoized result in the earlier call
    if (visited.has(r)) {
      return false;
    }

    visited.add(r);
    let res = true;

    for (const child of adjLists.get(r)) {
      if (adjLists.has(child)) {
        if (!canMake(child)) {
          res = false;
        }
      } else {
        if (!suppliesSet.has(child)) {
          res = false;
        }
      }

      if (!res) {
        break;
      }
    }

    memo.set(r, res);

    return res;
  };

  const result = [];

  for (const r of recipes) {
    if (canMake(r)) {
      result.push(r);
    }

    visited.clear();
  }

  return result;
};
// @leet end
