# @leet start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        WILDCARD_CHAR = "*"

        word_set = set(wordList) | {beginWord}

        if endWord not in word_set:
            return 0

        word_set.add(endWord)

        wildcard_to_words: dict[str, list[str]] = {}
        word_to_wildcards: dict[str, list[str]] = {}

        for word in word_set:
            word_to_wildcards[word] = []

            for i in range(len(word)):
                wildcard = word[:i] + WILDCARD_CHAR + word[i + 1 :]

                if wildcard not in wildcard_to_words:
                    wildcard_to_words[wildcard] = []

                wildcard_to_words[wildcard].append(word)
                word_to_wildcards[word].append(wildcard)

        visited = {beginWord}

        count = 1
        layer = [beginWord]

        while layer:
            count += 1
            next_layer: list[str] = []

            for source in layer:
                for wildcard in word_to_wildcards[source]:
                    if wildcard not in wildcard_to_words:
                        continue

                    for word in wildcard_to_words[wildcard]:
                        if word == endWord:
                            return count

                        if word not in visited:
                            next_layer.append(word)
                            visited.add(word)

                    # Optimization: don't iterate over same wildcard
                    # twice
                    del wildcard_to_words[wildcard]

            layer = next_layer

        return 0


# @leet end
