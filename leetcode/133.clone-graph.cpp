// @leet start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
#include <queue>
#include <unordered_map>

class Solution {
 public:
  Node* cloneGraph(Node* node) {
    if (!node) {
      return nullptr;
    }

    std::unordered_map<int, Node*> idxToCloneMap;
    idxToCloneMap[node->val] = new Node(node->val);

    std::queue<Node*> q;
    q.push(node);

    while (!q.empty()) {
      const auto* curr = q.front();
      auto* currClone = idxToCloneMap[curr->val];

      q.pop();

      for (auto* adj : curr->neighbors) {
        if (!idxToCloneMap.contains(adj->val)) {
          idxToCloneMap[adj->val] = new Node(adj->val);
          q.push(adj);
        }

        currClone->neighbors.push_back(idxToCloneMap[adj->val]);
      }
    }

    return idxToCloneMap[node->val];
  }
};
// @leet end
