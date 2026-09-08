// @leet start
/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
var accountsMerge = function (accounts) {
  const parents = new Map();
  const sizes = new Map();

  // Create disjoint set if it doesn't exist. Find the root of the
  // disjoint set. Do path compression.
  const find = (a) => {
    if (!parents.has(a)) {
      parents.set(a, a);
      sizes.set(a, 1);
    }

    if (parents.get(a) === a) {
      return a;
    }

    const root = find(parents.get(a));
    parents.set(a, root);

    return root;
  };

  // Merge the trees (by size) that contain a and b. If a and b don't
  // have their own set, make them. If a and b are already merged, don't
  // do anything.
  const union = (a, b) => {
    const rootA = find(a);
    const rootB = find(b);

    if (rootA === rootB) {
      return;
    }

    const rootASize = sizes.get(rootA);
    const rootBSize = sizes.get(rootB);

    if (rootASize <= rootBSize) {
      parents.set(rootA, rootB);
      sizes.set(rootB, rootASize + rootBSize);
    } else {
      parents.set(rootB, rootA);
      sizes.set(rootA, rootASize + rootBSize);
    }
  };

  const names = new Map();

  for (const account of accounts) {
    const name = account[0];

    names.set(account[1], name);
    find(account[1]);

    for (let i = 2; i < account.length; i++) {
      names.set(account[i], name);
      union(account[i - 1], account[i]);
    }
  }

  const mergedAccounts = new Map();

  for (const email of parents.keys()) {
    const root = find(email);

    if (!mergedAccounts.has(root)) {
      mergedAccounts.set(root, []);
    }

    mergedAccounts.get(root).push(email);
  }

  const result = [];

  for (const merged of mergedAccounts.values()) {
    result.push([names.get(merged[0]), ...merged.sort()]);
  }

  return result;
};
// @leet end
