// @leet start
#include <algorithm>
#include <limits>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

class Solution {
 public:
  int networkDelayTime(std::vector<std::vector<int>>& times, int n, int k) {
    const int INFTY = 1e9;

    // Build adjacency lists [(distance, edge),]
    std::unordered_map<int, std::vector<std::pair<int, int>>> edges;

    for (const auto& edgeVec : times) {
      edges[edgeVec[0] - 1].push_back({edgeVec[2], edgeVec[1] - 1});
    }

    // Use Djikstra's
    std::vector<int> dist(n, INFTY);
    std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                        std::greater<std::pair<int, int>>>
        pq;
    dist[k - 1] = 0;
    pq.push({0, k - 1});

    while (!pq.empty()) {
      const auto [pathDist, source] = pq.top();
      pq.pop();

      if (pathDist > dist[source]) {
        continue;
      }

      for (const auto& [weight, dest] : edges[source]) {
        const int newPathDist = pathDist + weight;

        if (newPathDist < dist[dest]) {
          dist[dest] = newPathDist;
          pq.push({newPathDist, dest});
        }
      }
    }

    int longestDistance = *std::max_element(dist.begin(), dist.end());

    return longestDistance < INFTY ? longestDistance : -1;
  }
};
// @leet end
