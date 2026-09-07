// @leet start
var Trie = function () {
  this.root = new Map();
  this.terminates = false;
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  this.insertHelper(word, 0);
};

Trie.prototype.insertHelper = function (word, start) {
  if (start === word.length) {
    this.terminates = true;
    return;
  }

  if (!this.root.has(word[start])) {
    this.root.set(word[start], new Trie());
  }

  this.root.get(word[start]).insertHelper(word, start + 1);
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  return this.searchHelper(word, 0);
};

Trie.prototype.searchHelper = function (word, start) {
  if (start === word.length) {
    return this.terminates;
  }

  if (!this.root.has(word[start])) {
    return false;
  }

  return this.root.get(word[start]).searchHelper(word, start + 1);
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  return this.startsWithHelper(prefix, 0);
};

Trie.prototype.startsWithHelper = function (prefix, start) {
  if (start === prefix.length) {
    return true;
  }

  if (!this.root.has(prefix[start])) {
    return false;
  }

  return this.root.get(prefix[start]).startsWithHelper(prefix, start + 1);
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
// @leet end
