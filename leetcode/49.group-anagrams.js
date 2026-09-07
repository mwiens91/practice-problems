// @leet start
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  const groups = new Map();

  for (const str of strs) {
    const key = [...str].sort().join("");

    if (groups.has(key)) {
      groups.get(key).push(str);
    } else {
      groups.set(key, [str]);
    }
  }

  const res = [];

  for (const group of groups.values()) {
    res.push(group);
  }

  return res;
};
// @leet end
