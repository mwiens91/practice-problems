// @leet start
#include <vector>

class Solution {
 public:
  vector<int> dailyTemperatures(vector<int>& temperatures) {
    std::vector<int> mono_stack;
    std::vector<int> result(temperatures.size());

    for (int i = temperatures.size() - 1; i >= 0; i--) {
      while (mono_stack.size() && temperatures[i] >= temperatures[mono_stack.back()]) {
        mono_stack.pop_back();
      }

      if (mono_stack.size()) {
        result[i] = mono_stack.back() - i;
      }

      mono_stack.push_back(i);
    }

    return result;
  }
};
// @leet end
