// @leet start
#include <cstddef>
#include <queue>
#include <vector>

class Solution {
 public:
  bool isBipartite(std::vector<std::vector<int>>& graph) {
    const std::size_t n = graph.size();
    std::vector<bool> visited(n, false);
    std::vector<bool> layerEven(n, false);

    // Define lambda to perform BFS on a component, returning true
    // if the component is bipartite, or short-circuiting early and
    // returning false if not
    auto isComponentBipartite = [&](int start) -> bool {
      visited[start] = true;

      std::queue<int> q;
      q.push(start);

      while (!q.empty()) {
        const int v = q.front();
        q.pop();

        for (const int vAdj : graph[v]) {
          if (!visited[vAdj]) {
            visited[vAdj] = true;
            layerEven[vAdj] = !layerEven[v];
            q.push(vAdj);
          } else if (layerEven[v] == layerEven[vAdj]) {
            return false;
          }
        }
      }

      return true;
    };

    // Return false if any component is bipartite
    for (std::size_t v = 0; v < n; v++) {
      if (!visited[v] && !isComponentBipartite(v)) {
        return false;
      }
    }

    return true;
  }
};
// @leet end
