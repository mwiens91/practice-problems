// @leet start
class Trie {
  // 27th child is to encode a word terminates here
  private readonly children: (Trie | null)[] = new Array(27).fill(null);

  insert(word: string): void {
    const idx = Trie.getChildIndex(word);

    if (!this.children[idx]) {
      this.children[idx] = new Trie();
    }

    if (word.length) {
      this.children[idx].insert(word.slice(1));
    }
  }

  search(word: string): boolean {
    const idx = Trie.getChildIndex(word);

    return (
      this.children[idx] !== null &&
      (!word.length || this.children[idx].search(word.slice(1)))
    );
  }

  startsWith(prefix: string): boolean {
    if (!prefix.length) {
      return true;
    }

    const idx = Trie.getChildIndex(prefix);

    return (
      this.children[idx] !== null &&
      this.children[idx].startsWith(prefix.slice(1))
    );
  }

  private static getChildIndex(word: string): number {
    return word.length ? word.charCodeAt(0) - "a".charCodeAt(0) : 26;
  }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
// @leet end
