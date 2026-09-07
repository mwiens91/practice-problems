// @leet start
/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const adjLists = Array.from({ length: numCourses }, () => []);

  for (const [to, from] of prerequisites) {
    adjLists[from].push(to);
  }

  const seen = Array(numCourses).fill(false);
  const processing = Array(numCourses).fill(false);

  // Return true if cycle, else false
  const dfs = (start) => {
    const stack = [start];
    seen[start] = true;

    while (stack.length) {
      const curr = stack.pop();

      // If marked as processing, unmark and continue. Else mark as
      // processing, push to stack.
      if (processing[curr]) {
        processing[curr] = false;
        continue;
      }

      processing[curr] = true;
      stack.push(curr);

      // Push children to stack
      for (const child of adjLists[curr]) {
        // If child is being processed, it's a cycle; if child not
        // seen, mark as seen and push to stack
        if (processing[child]) {
          return true;
        }

        if (!seen[child]) {
          seen[child] = true;
          stack.push(child);
        }
      }
    }

    return false;
  };

  for (let course = 0; course < numCourses; course++) {
    if (!seen[course] && dfs(course)) {
      return false;
    }
  }

  return true;
};
// @leet end
