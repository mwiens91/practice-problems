// @leet start
#include <algorithm>
#include <string>
#include <vector>

class Solution {
 public:
  int garbageCollection(std::vector<std::string>& garbage, std::vector<int>& travel) {
    // There's a better way of doing this but I'm tired
    int result = 0;

    for (char type : {'M', 'P', 'G'}) {
      result += timeToGetTrashType(garbage, travel, type);
    }

    return result;
  }

 private:
  int timeToGetTrashType(const std::vector<std::string>& garbage, const std::vector<int>& travel,
                         char trashType) {
    int time = 0;
    int travelTimeToIdx = 0;

    for (size_t i = 0; i < garbage.size(); i++) {
      int count = std::count(garbage[i].begin(), garbage[i].end(), trashType);

      if (count > 0) {
        time += count + travelTimeToIdx;
        travelTimeToIdx = 0;
      }

      if (i < travel.size()) {
        travelTimeToIdx += travel[i];
      }
    }

    return time;
  }
};
// @leet end
