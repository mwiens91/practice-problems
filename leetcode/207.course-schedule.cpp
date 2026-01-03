// @leet start
#include <cstddef>
#include <queue>
#include <vector>

class Solution {
 public:
  bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) {
    std::vector<std::vector<std::size_t>> graph(numCourses);
    std::vector<int> inDegree(numCourses);

    for (const auto& prerequisite : prerequisites) {
      graph[prerequisite[1]].push_back(prerequisite[0]);
      inDegree[prerequisite[0]]++;
    }

    std::queue<std::size_t> q;

    for (std::size_t i = 0; i < numCourses; i++) {
      if (!inDegree[i]) {
        q.push(i);
      }
    }

    while (!q.empty()) {
      const auto curr = q.front();
      q.pop();

      for (const auto adj : graph[curr]) {
        inDegree[adj]--;

        if (!inDegree[adj]) {
          q.push(adj);
        }
      }
    }

    for (std::size_t i = 0; i < numCourses; i++) {
      if (inDegree[i]) {
        return false;
      }
    }

    return true;
  }
};
// @leet end
