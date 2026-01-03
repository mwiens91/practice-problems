// @leet start
#include <algorithm>
#include <cstddef>
#include <queue>
#include <tuple>
#include <vector>

class Solution {
 public:
  int orangesRotting(std::vector<std::vector<int>>& grid) {
    std::vector<std::tuple<int, int>> dirs{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    std::queue<std::tuple<std::size_t, std::size_t, int>> q;

    for (std::size_t row = 0; row < grid.size(); row++) {
      for (std::size_t col = 0; col < grid[0].size(); col++) {
        if (grid[row][col] == 2) {
          q.push({row, col, 0});
        }
      }
    }

    int maxTime = 0;

    while (!q.empty()) {
      const auto [row, col, time] = q.front();
      q.pop();

      for (const auto [dx, dy] : dirs) {
        const int newRow = row + dx;
        const int newCol = col + dy;

        if (newRow >= 0 && newRow < grid.size() && newCol >= 0 && newCol < grid[0].size() &&
            grid[newRow][newCol] == 1) {
          grid[newRow][newCol] = 2;

          const int newTime = time + 1;
          maxTime = std::max(maxTime, newTime);
          q.push({newRow, newCol, newTime});
        }
      }
    }

    for (std::size_t row = 0; row < grid.size(); row++) {
      for (std::size_t col = 0; col < grid[0].size(); col++) {
        if (grid[row][col] == 1) {
          return -1;
        }
      }
    }

    return maxTime;
  }
};
// @leet end
