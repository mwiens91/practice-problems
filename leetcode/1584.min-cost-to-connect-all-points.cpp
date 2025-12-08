// @leet start
#include <cmath>
#include <functional>
#include <queue>
#include <utility>
#include <vector>

class Solution {
 public:
  int minCostConnectPoints(std::vector<std::vector<int>>& points) {
    // Use Prim's algorithm: start with node 0
    std::priority_queue<std::pair<int, size_t>, std::vector<std::pair<int, size_t>>,
                        std::greater<std::pair<int, size_t>>>
        pq;
    std::vector<bool> visited(points.size());
    visited[0] = true;

    auto addEdges = [&](size_t node) {
      for (size_t i = 0; i < points.size(); i++) {
        if (!visited[i]) {
          pq.push(
              {std::abs(points[node][0] - points[i][0]) + std::abs(points[node][1] - points[i][1]),
               i});
        }
      }
    };
    addEdges(0);

    int totalWeight = 0;
    int count = 1;

    while (count < points.size()) {
      const auto [weight, node] = pq.top();
      pq.pop();

      if (visited[node]) {
        continue;
      }

      visited[node] = true;
      addEdges(node);
      count += 1;
      totalWeight += weight;
    }

    return totalWeight;
  }
};
// @leet end
