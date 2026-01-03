// @leet start
#include <queue>
#include <utility>
#include <vector>

class Solution {
 public:
  std::vector<std::vector<int>> kClosest(std::vector<std::vector<int>>& points, int k) {
    std::priority_queue<std::pair<int, int>> pq;  // dist, idx

    for (int i = 0; i < points.size(); i++) {
      pq.push({points[i][0] * points[i][0] + points[i][1] * points[i][1], i});

      if (pq.size() > k) {
        pq.pop();
      }
    }

    std::vector<std::vector<int>> result;

    for (; k > 0; k--) {
      result.push_back(points[pq.top().second]);
      pq.pop();
    }

    return result;
  }
};
// @leet end
